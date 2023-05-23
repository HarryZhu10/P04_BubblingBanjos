

var map = L.map('map').setView([40.70850, -74.00603], 13); //40.70850/-74.00603

function getColor(d) {
    return d > 1000 ? '#800026' :
    d > 500  ? '#BD0026' :
    d > 200  ? '#E31A1C' :
    d > 100  ? '#FC4E2A' :
    d > 50   ? '#FD8D3C' :
    d > 20   ? '#FEB24C' :
    d > 10   ? '#FED976' :
               '#FFEDA0';
}

function style(feature) {
    return {
        fillcolor: getColor(feature.properties.density), //<-- We replace .properties.density with what ever data we will be looking at such as 
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
} //this function will set the color basedn

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// add the states polygon data to the map
var data = document.getElementById("data");

json_data = JSON.parse(data.innerHTML);
var statesData = json_data;

console.log(data.innerHTML);
console.log(statesData);
console.log('hello!');

// L.geoJson(statesData).addTo(map);

L.geoJson(statesData, {style: style}).addTo(map);

// end of the states polylgon data code

// to add a bunch of markers to the map

var points_data = document.getElementById("points");
// console.log(points_data);
json_points = JSON.parse(points_data.innerHTML);
console.log(json_points[5])

//marker colors
var normal = "";
var orange = "invert(62%) sepia(22%) saturate(2096%) hue-rotate(1deg) brightness(104%) contrast(104%)";
var red = "invert(94%) sepia(56%) saturate(2798%) hue-rotate(353deg) brightness(102%) contrast(104%)";
var yellow = "invert(12%) sepia(83%) saturate(6686%) hue-rotate(1deg) brightness(111%) contrast(117%)";
var purple = "invert(7%) sepia(100%) saturate(7307%) hue-rotate(247deg) brightness(113%) contrast(145%)";
var alien = "invert(32%) sepia(35%) saturate(504%) hue-rotate(78deg) brightness(91%) contrast(93%)"

const colorList = [normal, orange, red, yellow, purple, alien];


var testGroup =  L.layerGroup().addTo(map); //create a layer allows us to put markers into different groups for easier customization

for (let i = 0; i < json_points.length; i++) {
    // console.log(json_points[i])
    var mark = L.marker(json_points[i]).addTo(testGroup);
    mark.getElement().style.filter = normal;
    // console.log(mark.getLatLng())
    var popup_string = "<b>Hello world!</b><br>I am a popup.<br>My coordinate is " + mark.getLatLng()["lat"] + ", " + mark.getLatLng()["lng"];
    mark.bindPopup(popup_string).openPopup();
  } 

var colorButton = document.getElementById('colorChanger');
colorButton.addEventListener('click', function() {
    console.log("button clicked!");
    var randomColor = Math.floor(Math.random()*5);
    testGroup.eachLayer(function (marker) { // .eachLayer goes through every object that was added to it. In this case the markers
        marker.getElement().style.filter = colorList[randomColor]; //altering the color of the markers
    });
});

var selectDropdown = document.getElementById('colorSelector1');
selectDropdown.addEventListener('input', function() {
    testGroup.eachLayer(function(marker) {
        marker.getElement().style.filter = colorList[selectDropdown.value];
    });
})

var displayBtn = document.getElementById('collisionDisplay1');
displayBtn.addEventListener('input', () => {
    testGroup.eachLayer(function(marker) {
        marker.getElement().style.visibility = 'visible';
        marker._shadow.style.visibility = 'visible';
    });
});

var hideBtn = document.getElementById('collisionDisplay2');
hideBtn.addEventListener('input', () => {
    testGroup.eachLayer(function(marker) {
        marker.getElement().style.visibility = 'hidden';
        marker._shadow.style.visibility = 'hidden';
    });
});



// end of mass markers code

var marker = L.marker([40.70850, -74.00603]).addTo(map);
marker.getElement().style.filter =  "invert(62%) sepia(22%) saturate(2096%) hue-rotate(1deg) brightness(104%) contrast(104%)";
//<- can change the color of the marker by altering attribute of style.filter
// examples of style.filter attributes: none | blur() | brightness() | contrast() | drop-shadow() | grayscale() | hue-rotate() | invert() | opacity() | saturate() | sepia()

var circle = L.circle([40.72850, -74.00603], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);

var polygon = L.polygon([
    [40.7819063, -73.9829206],
    [40.7704018,-73.9915037],
    [40.7639338,-73.9716339]
], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
}).addTo(map);

marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
circle.bindPopup("I am a circle.");
polygon.bindPopup("I am a polygon.");

function onMapClick(e) {
    console.log("You clicked the map at " + e.latlng);
}

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);


//function for dynamic slider values

// NYC Motor Vehicle Collisions
const slider1 = document.getElementById("slider1");
const sliderLabel1 = document.getElementById("label1");
sliderLabel1.textContent = Number(slider1.value) + 2000; //sets label to default slider value

slider1.addEventListener('input', function() {
    console.log(slider1.value);
    sliderLabel1.textContent = Number(slider1.value) + 2000; //added number is the lowest year
});

// NYC Shootings
const slider2 = document.getElementById("slider2");
const sliderLabel2 = document.getElementById("label2");
sliderLabel2.textContent = Number(slider2.value) + 2000; //sets label to default slider value

slider2.addEventListener('input', function() {
    console.log(slider2.value);
    sliderLabel2.textContent = Number(slider2.value) + 2000; //added number is the lowest year
});

// NYC Arrests
const slider3 = document.getElementById("slider3");
const sliderLabel3 = document.getElementById("label3");
sliderLabel3.textContent = Number(slider3.value) + 2000; //sets label to default slider value

slider3.addEventListener('input', function() {
    console.log(slider3.value);
    sliderLabel3.textContent = Number(slider3.value) + 2000; //added number is the lowest year
});


var map = L.map('map').setView([40.70850, -74.00603], 13); //40.70850/-74.00603


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

L.geoJson(statesData).addTo(map);

// end of the states polylgon data code

// to add a bunch of markers to the map

var points_data = document.getElementById("points");
// console.log(points_data);
json_points = JSON.parse(points_data.innerHTML);
console.log(json_points[5])

for (let i = 0; i < json_points.length; i++) {
    // console.log(json_points[i])
    var mark = L.marker(json_points[i]).addTo(map);
    // console.log(mark.getLatLng())
    var popup_string = "<b>Hello world!</b><br>I am a popup.<br>My coordinate is " + mark.getLatLng()["lat"] + ", " + mark.getLatLng()["lng"];
    mark.bindPopup(popup_string).openPopup();
  } 

// end of mass markers code

var marker = L.marker([40.70850, -74.00603]).addTo(map);

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

// NYC Hate Crimes
const slider2 = document.getElementById("slider2");
const sliderLabel2 = document.getElementById("label2");
sliderLabel2.textContent = Number(slider2.value) + 2000; //sets label to default slider value

slider2.addEventListener('input', function() {
    console.log(slider2.value);
    sliderLabel2.textContent = Number(slider2.value) + 2000; //added number is the lowest year
});

// NYC shooting incidents
const slider3 = document.getElementById("slider3");
const sliderLabel3 = document.getElementById("label3");
sliderLabel3.textContent = Number(slider3.value) + 2000; //sets label to default slider value

slider3.addEventListener('input', function() {
    console.log(slider3.value);
    sliderLabel3.textContent = Number(slider3.value) + 2000; //added number is the lowest year
});

// NYC Arrest Data
const slider4 = document.getElementById("slider4");
const sliderLabel4 = document.getElementById("label4");
sliderLabel4.textContent = Number(slider4.value) + 2000; //sets label to default slider value

slider4.addEventListener('input', function() {
    console.log(slider4.value);
    sliderLabel4.textContent = Number(slider4.value) + 2000; //added number is the lowest year
});
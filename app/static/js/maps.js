

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

// L.geoJson(statesData, {style: style}).addTo(map);

// end of the states polylgon data code

// to add a bunch of markers to the map

var points_data = document.getElementById("points");
// console.log(points_data);
json_points = JSON.parse(points_data.innerHTML);
console.log(json_points[5])
var col_points = document.getElementById("collision_points");
json_col_points = JSON.parse(col_points.innerHTML);
var sho_points = document.getElementById("shooting_points");
json_sho_points = JSON.parse(sho_points.innerHTML);
var arr_points = document.getElementById("arrest_points");
json_arr_points = JSON.parse(arr_points.innerHTML);

//marker colors
var normal = "";
var orange = "invert(62%) sepia(22%) saturate(2096%) hue-rotate(1deg) brightness(104%) contrast(104%)";
var red = "invert(94%) sepia(56%) saturate(2798%) hue-rotate(353deg) brightness(102%) contrast(104%)";
var yellow = "invert(12%) sepia(83%) saturate(6686%) hue-rotate(1deg) brightness(111%) contrast(117%)";
var purple = "invert(7%) sepia(100%) saturate(7307%) hue-rotate(247deg) brightness(113%) contrast(145%)";
var alien = "invert(32%) sepia(35%) saturate(504%) hue-rotate(78deg) brightness(91%) contrast(93%)"

//color values retrieved with the help of https://codepen.io/sosuke/pen/Pjoqqp (CSS filter generator to convert from black to target hex color)

const colorList = [normal, orange, red, yellow, purple, alien];



/* ================================================================================ PLOTTING POINTS ON MAP ================================================================================ */
// console.log("COLLISION: " + json_col_points[1]);
var collisionGroup = L.layerGroup().addTo(map);
for (let i = 0; i < json_col_points.length; i++) {
    if (json_col_points[i][3].substring(0,9) == "2022-05-1" ) {
        var mark = L.marker([json_col_points[i][1], json_col_points[i][2]]).addTo(collisionGroup);
        mark.getElement().style.filter = normal;
        var popup_string = "<b>Additional Info</b><br> <b>Coordinates:</b> [" + json_col_points[i][1] + ", " + json_col_points[i][2] + "]<br> <b>Crash Time:</b> " + json_col_points[i][4] + "<br><b>Number of Persons Injured:</b> " + json_col_points[i][6] + "<br><b>Number of Persons Killed:</b> " + json_col_points[i][7] + "<br> <b>Vehicle Type:</b> " + json_col_points[i][8];
        mark.bindPopup(popup_string);
    }
}

var shootingsGroup = L.layerGroup().addTo(map);
for (let i = 0; i < json_sho_points.length; i++) {
    if (json_sho_points[i][3].substring(0,9) == "2022-05-1") {
        var mark = L.marker([json_sho_points[i][1], json_sho_points[i][2]]).addTo(shootingsGroup);
        mark.getElement().style.filter = normal;
        var popup_string = "<b>Additional Info</b><br> <b>Coordinates:</b> [" + json_sho_points[i][1] + ", " + json_sho_points[i][2] + "]<br> <b>Perpetrator's Age Group:</b> " + json_sho_points[i][4] + "<br><b>Perpetrator's Sex:</b> " + json_sho_points[i][5] + "<br><b>Perpetrator's Race:</b>" + json_sho_points[i][6]+ "<br><b>Victim's Age Group:</b> " + json_sho_points[i][7] + "<br><b>Victim's Sex:</b> " + json_sho_points[i][8] + "<br><b>Victim's Race:</b> " + json_sho_points[i][9];
        mark.bindPopup(popup_string);
    }
}

/* ================================================================================ NAV BAR SCRIPT ================================================================================ */

 
//script for changing the color of markers

var selectDropdownCollision = document.getElementById('colorSelector1');
selectDropdownCollision.addEventListener('input', function() {
    collisionGroup.eachLayer(function(marker) {
        marker.getElement().style.filter = colorList[selectDropdownCollision.value];
    });
});

var selectDropdownShootings = document.getElementById('colorSelector2');
selectDropdownShootings.addEventListener('input', function() {
    shootingsGroup.eachLayer(function(marker) {
        marker.getElement().style.filter = colorList[selectDropdownShootings.value];
    });
});


//script for displaying/hiding markers

var displayBtnCollision = document.getElementById('collisionDisplay1');
displayBtnCollision.addEventListener('input', () => {
    collisionGroup.eachLayer(function(marker) {
        marker.getElement().style.visibility = 'visible';
        marker._shadow.style.visibility = 'visible';
    });
});

var hideBtnCollison = document.getElementById('collisionDisplay2');
hideBtnCollison.addEventListener('input', () => {
    collisionGroup.eachLayer(function(marker) {
        marker.getElement().style.visibility = 'hidden';
        marker._shadow.style.visibility = 'hidden';
    });
});

var displayBtnShootings = document.getElementById('shootingsDisplay1');
displayBtnShootings.addEventListener('input', () => {
    shootingsGroup.eachLayer(function(marker) {
        marker.getElement().style.visibility = 'visible';
        marker._shadow.style.visibility = 'visible';
    });
});

var hideBtnShootings = document.getElementById('shootingsDisplay2');
hideBtnShootings.addEventListener('input', () => {
    shootingsGroup.eachLayer(function(marker) {
        marker.getElement().style.visibility = 'hidden';
        marker._shadow.style.visibility = 'hidden';
    });
});




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
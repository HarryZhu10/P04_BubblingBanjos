var data = document.getElementById("data");

json_data = JSON.parse(data.innerHTML);
var statesData = json_data;

console.log(data.innerHTML);
console.log(statesData);
console.log('hello!');

// console.log(statesData)

var map = L.map('map').setView([40.70850, -74.00603], 13); //40.70850/-74.00603


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

L.geoJson(statesData).addTo(map);

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
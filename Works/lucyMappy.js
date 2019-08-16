var map;
var ourLoc;
var view;

function init(){
  ourLoc = ol.proj.fromLonLat([-7.77832031, 53.2734]);
  view = new ol.View({
    center: ourLoc,
    zoom: 6
  });
  map = new ol.Map({
    target:'map',
    layers:[
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view:view
  });
}

function panHome(){
  view.animate({
    center:ourLoc,
    duration:2000
  });
}

function panToLocation(){
  var countryName = document.getElementById("country-name").value;
  var query = "https://restcountries.eu/rest/v2/name/"+countryName;
  var lon= 0.0;
  var lat= 0.0;
  var location= ol.proj.fromLonLat([lon,lat]);
  view.animate({
    center: location,
    duration: 2000
  });
}

window.onload = init;

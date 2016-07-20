
//globals for handling user 
var ready = null;
var am_or_fm = 'fm'
var mymap = L.map('mapid');


// throttle requests for contours
setInterval( function() {
    if (ready == true) {
        get_json('', null);
    }
    ready = false
    }, 1000);



var geojsonMarkerOptions = {
    radius: 300,
    fillColor: "#f33",
    color: "#f33",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};
var myStyle = {
                "color": "#8000f0"
};

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: 
    '&copy; \
    <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

// so we can clear it at each load event
var geojson_layer = null;
// for contour and 
var popup = L.marker();
var popup2 = L.marker();

function combine_json(old_json, new_json){
}

function pretty_json(json){
    var s = ""
    for (var key in json) {
        s += key + ": " + json[key] + "<br>";
    
    }
    return s;
    }

function get_json(auto, e) {
    if (auto === 'auto'){
        console.log('yeah')
        //need to think about waiting for autopan
    }
    console.log("TEST STATIC4");
    bounds = mymap.getBounds()
    old_json = null;
    $.getJSON(
        '/json', { 'w':bounds.getWest(),'s':bounds.getSouth(),
        'e': bounds.getEast(), 'n': bounds.getNorth(), 'type':am_or_fm},          
        function( test_json ) {
                        
            if(geojson_layer !== null) { 
                mymap.removeLayer(geojson_layer); 
            }
            
            geojson_layer = L.geoJson(test_json, {
                pointToLayer: function (feature, latlng) {
                    return L.circle(latlng, 300, geojsonMarkerOptions)
                        .on('mouseover', function(e){
                            e.target.setRadius(1000);
                        })
                        .on('mouseout', function(e){
                            e.target.setRadius(300);
                        })
                },
                style: myStyle,
                onEachFeature: function (feature, layer) {
                    // add_general on click, not mouseover
                    var coords = 
                        feature.geometry.geometries[0].coordinates
                    var coords2 = 
                        feature.geometry.geometries[1].coordinates[0]
                    var latlng = L.latLng(coords[1], coords[0]);
                    var latlng2 = L.latLng(coords2[1], coords2[0]);
                    layer.on('click', function(e){
                        popup.setLatLng(latlng)
                        //.setContent(JSON.stringify(feature.properties));
                        popup2.setLatLng(latlng2)
                        //.setContent(JSON.stringify(feature.properties));
                        mymap.addLayer(popup);
                        mymap.addLayer(popup2)
                        
                        $('#info_span').html(pretty_json(feature.properties));
                    })
                }  
        })
        old_json = test_json;
        geojson_layer.addTo(mymap);
    })
}

function fullscreenit(element) {
  if(element.requestFullscreen) {
    element.requestFullscreen();
  } else if(element.mozRequestFullScreen) {
    element.mozRequestFullScreen();
  } else if(element.webkitRequestFullscreen) {
    element.webkitRequestFullscreen();
  }
}

//deal with am and fm switch 
$(function() {           
    $('#typeform').on('change', function() {
        type = $('input[name=typeG]:checked', '#typeform').val();
        console.log(type);
        am_or_fm = type;
        //get_json('', null)
        if (am_or_fm == 'am'){
            myStyle = { "color": "#ff0000"};
        } else {
            myStyle = { "color": "#8000f0"};
        }
            
        get_json('auto', null)
    })
    //navigator.geolocation.getCurrentPosition(yes, no)
    var fsbtn = document.getElementById("fsbtn");
    var map_elem = document.getElementById("mapid");
    fsbtn.addEventListener("click", function() {
      fullscreenit(document.documentElement)
    }, false);
})
 
 
/*
function clear_popups(){
    mymap.removeLayer(popup); 
    mymap.removeLayer(popup2);
    }
*/
     
mymap.on('dragend', function() {
    ready = true;
})
mymap.on('zoomend', function() {
    // there is a zoom on start so this is extraneous
    //mymap.on('load', function()
    //initial load
    if(ready == null) { 
        get_json('', null)
    } else {
        ready = true;
    }
})
mymap.on('autopanstart', function(e) {
    ready = true;
})

mymap.setMaxBounds(L.latLngBounds(L.latLng(-85,-180), L.latLng(85,180.0)));

function onLocationFound(e) {
    var radius = e.accuracy / 2;

    L.marker(e.latlng).addTo(mymap)
        

    L.circle(e.latlng, radius).addTo(mymap);
}

mymap.on('locationfound', onLocationFound);

function onLocationError(e) {
    mymap.setView([35.0820878,-106.956667], 7);
    console.log('test' + e.message)
}


mymap.on('locationerror', onLocationError);

mymap.locate({setView: true, maxZoom: 7});








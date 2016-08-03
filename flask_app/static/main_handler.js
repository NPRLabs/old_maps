
// what kind of contours to display
var am_or_fm = 'fm';

var map = L.map('mapid', {autoZIndex:false});


/* 
    limit getting geojson requests to one second a zoom and then immediatly a
    drag will get json once. This is a really simple and effective optimization
*/

var ready = null;
setInterval( function() {
    if (ready == true) {
        redraw('', null);
    }
    ready = false
    }, 1000);


/* Global Style Options */
var geojsoncenterMarkerOptions = {
    radius: 2,
    fillColor: "#f33",
    color: "#f33",
    weight: 1,
    opacity: 1,
    fillOpacity: 1
};

var fmStyle = { 
    radius: 6,
    "color": "#8000f0",
    "fillColor": "#8000f0",
    "fillOpacity": 1.0,
    weight:9,
    stroke:true
};
var fmStyleFilled = { 
    radius: 2,
    "color": "#4D00BD",
    "fillColor": "#8000f0",
    "fillOpacity": 0.2,
    weight:3,
    opacity: 1,
    stroke:true
    //stroke:false
};
var amStyle = { 
    radius: 6,
    "color": "#ff0000",
    "fillColor": "#ff0000",
    "fillOpacity": 1.0,
    weight:9,
    stroke:true
};
var amStyleFilled = { 
    radius: 2,
    "color": "#990000",
    "fillColor": "#ff0000",
    "fillOpacity": 0.2,
    weight:3,
    opacity: 1,
    stroke:true
    //stroke:false
};

// for clearing double-drawn features
var clearStyle = { stroke:false };

var contourStyle = fmStyle;
var contourStyleFilled = fmStyleFilled;


// set up the OSM tiles
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: 
    '&copy; \
    <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


var geojsonLayer = null;
var selectedGeojson = null;
var selectedFeature = null;
var hiddenContourLayer = null;


var centerMarker = L.marker();
var contourMarker = L.marker();


function pretty_json(json){
    var s = "";
    for (var key in json) {
        s += key + ": " + json[key] + "<br>";
    
    }
    return s;
}

function compareFeatureCenters(f, d) {
    var test1 = f.geometry.geometries[0]['coordinates'][0] 
                == d.geometry.geometries[0]['coordinates'][0];
    var test2 = f.geometry.geometries[0]['coordinates'][1] 
                == d.geometry.geometries[0]['coordinates'][1];
    return test1 && test2;
}

function redraw(auto, e) {
    if (auto === 'auto'){
        //console.log('yeah')
        //need to think about waiting for autopan
    }
    
    bounds = map.getBounds()
    $.getJSON(
        '/json', { 'w':bounds.getWest(),'s':bounds.getSouth(),
        'e': bounds.getEast(), 'n': bounds.getNorth(), 'type':am_or_fm},          
        function( test_json ) {
            //console.log(test_json);
            //f_flag = null;            
            if(geojsonLayer !== null) { 
                map.removeLayer(geojsonLayer); 
            }
            
            geojsonLayer = L.geoJson(test_json, {
                pointToLayer: function (feature, latlng) {
                    //return //L.circle(latlng, 300, geojsoncenterMarkerOptions)
                    return L.circleMarker(latlng, geojsoncenterMarkerOptions)
                        //.on('mouseover', function(e){
                        //    e.target.setRadius(1000);
                       // })
                       // .on('mouseout', function(e){
                       //     e.target.setRadius(300);
                       // })
                },
                style: contourStyle,
                onEachFeature: function (feature, layer) {
                    // add_general on click, not mouseover
                    var coords = 
                        feature.geometry.geometries[0].coordinates
                    var coords2 = 
                        feature.geometry.geometries[1].coordinates[0]
                    var latlng = L.latLng(coords[1], coords[0]);
                    var latlng2 = L.latLng(coords2[1], coords2[0]);
                    
                    console.log(layer.feature.properties)
                    console.log(layer.feature.id)
                    layer.on('click', function(e){
                        coords = layer.feature.geometry
                                    .geometries[1].coordinates
                                    
                        //(filled) Polygon of the selected feature      
                        new_poly = {
                            type: "Feature",
                            properties: layer.feature.properties,
                            geometry: {
                                geometries: [
                                    layer.feature.geometry.geometries[0],
                                    {
                                        type: "Polygon",
                                        coordinates: [coords]
                                    }
                                    ],
                                    type: "GeometryCollection"
                                }
                            
                        };
                        
                        if (selectedGeojson !== null) {
                            map.removeLayer(selectedGeojson);
                        }
                        
                        
                        if (hiddenContourLayer !== null) {
                            hiddenContourLayer.setStyle(contourStyle);
                            geojsonLayer.setStyle(contourStyle);
                        } 
                        
                        layer.setStyle(clearStyle);
                        selectedGeojson = L.geoJson(new_poly, {
                            style: contourStyleFilled,
                            pointToLayer: function (feature, latlng) {
                    
                                return L.circleMarker(latlng,
                                     geojsoncenterMarkerOptions)

                            }
                        })
                            
                        // hacky way of ordering
                        map.removeLayer(geojsonLayer);
                        selectedGeojson.addTo(map); 
                        geojsonLayer.addTo(map); 

                        //setcenterMarkers and add info
                        centerMarker.setLatLng(latlng)
                        contourMarker.setLatLng(latlng2)
                        map.addLayer(centerMarker);
                        // with changing colors no need
                        //map.addLayer(contourMarker);
                        $('#info_span').html(pretty_json(feature.properties));
                        
                        hiddenContourLayer = layer
                        selectedFeature = feature
                        
                    })
                    
                    if (selectedFeature !== null 
                            && compareFeatureCenters(selectedFeature, feature)){
                        layer.setStyle(clearStyle);
                    }
                    
                }  
        })
        
        if(selectedGeojson !== null){
            map.removeLayer(geojsonLayer);
            selectedGeojson.addTo(map);
        }    
        geojsonLayer.addTo(map);
            
    })
}


//deal with am and fm switch 
$(function() {           
    $('#typeform').on('change', function() {
        type = $('input[name=typeG]:checked', '#typeform').val();
        am_or_fm = type;
        map.removeLayer(centerMarker); 
        map.removeLayer(contourMarker);
        //redraw('', null)
        if (am_or_fm == 'am'){
            contourStyle = amStyle;
            contourStyleFilled = amStyleFilled;
        } else {
            contourStyle = fmStyle;
            contourStyleFilled = fmStyleFilled;
        }
        
        
        selectedFeature = null;
        if(selectedGeojson !== null){
            map.removeLayer(selectedGeojson);
        }
        selectedGeojson = null;
            
        redraw('auto', null)
    })
})
 
 
     
map.on('dragend', function() {
    ready = true;
})
map.on('zoomend', function() {
    // there is a zoom on start so this is extraneous
    //map.on('load', function()
    //initial load
    if(ready == null) { 
        redraw('', null)
    } else {
        ready = true;
    }
})
map.on('autopanstart', function(e) {
    ready = true;
})

map.setMaxBounds(L.latLngBounds(L.latLng(-85,-180), L.latLng(85,180.0)));

function onLocationFound(e) {
    var radius = e.accuracy / 2;

    L.marker(e.latlng).addTo(map)
        

    L.circle(e.latlng, radius).addTo(map);
}

map.on('locationfound', onLocationFound);

function onLocationError(e) {
    // abq!
    map.setView([35.0820878,-106.956667], 7);
    console.log('test' + e.message)
}


map.on('locationerror', onLocationError);

map.locate({setView: true, maxZoom: 7});

$(function() {           
    $('#geocodebtn').on('click', function() {
        $.ajax(
            {
                url:"/geocode?q=" + encodeURI($('#address_input').val()), 
                success: function(data) { 
                console.log(data)
                var marker = new L.marker(data.split(','))
                    marker.on('click', function(e) {
                        map.removeLayer(marker);
                    })
                    marker.addTo(map);
                    
                    map.setView(data.split(','), 13) 
                    redraw('', null)}
                })
    })
    $('#csbtn').on('click', function() {
        $.ajax(
            {
                url:"/callsign?cs=" 
                        + encodeURI($('#address_input').val())
                        + "&type=" + am_or_fm, 
                success: function(data) { 
                    console.log(data)
                    map.setView(data.replace(/[{}]/g, "").split(','), 13) 
                    }
                })
    })
})







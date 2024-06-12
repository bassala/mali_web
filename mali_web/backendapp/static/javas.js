


// Initialisation de la carte
var map = L.map('map', {editable: true}).setView([17.570692,-3.996166], 5.5);

// Ajout des couches de tuiles
var Osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'});
var fontTopo =  L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    maxZoom: 17,
    attribution: 'Map data: {attribution.OpenStreetMap}, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});

// Ajout de la couche GeoJSON pour le Mali
var mali = L.geoJSON(maliJSON, {
    style: style,
    onEachFeature: function(feature, layer) {
        layer.bindPopup(feature.properties.NAME_1); // Lie le nom de la région au popup
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight,
            click: zoomToFeature
        });
    }
}).addTo(map);



// Contrôle des couches de base
var baseMaps = {
    "OpenStreetMap": Osm,
    "fontTopo" : fontTopo,
};
var layerControl = L.control.layers(baseMaps).addTo(map);




// Fonction pour déterminer la couleur en fonction du nom de la région
function getColor(r_name) {
    switch (r_name) {
        case "Bamako": return '#800026';
        case "Gao"   : return '#BD0026';
        case "Kayes" : return '#E31A1C';
        case "Kidal" : return '#FC4E2A';
        case  "Koulikoro": return '#FD8D3C';
        case "Mopti": return '#FEB24C';
        case  "Ségou":return '#FED976';
        case  "Sikasso": return '#FED986';
        case "Timbuktu" : return '#FED987';
    }
}

// Style des régions
function style(feature) {
    return {
        fillColor: getColor(feature.properties.NAME_1),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

// Gestion des événements pour chaque région
function highlightFeature(e) {
    var layer = e.target;
    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });
    layer.bringToFront();
}

function resetHighlight(e) {
    mali.resetStyle(e.target);
}

// Fonction pour récupérer les données de la région sélectionnée
function getRegionModel(regionName) {
    var regionModels = {
        "Bamako": "Bamako",
        "Gao": "Gao",
        "Kidal": "Kidal",
        "Koulikoro": "Koulikoro",
        "Mopti": "Mopti",
        "Ségou": "Ségou",
        "Sikasso": "Sikasso",
        "Timbuktu": "Timbuktu",
        "Kayes": "Kayes"
    };
    return regionModels[regionName];
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
    var regionName = e.target.feature.properties.NAME_1;
    var modelName = getRegionModel(regionName);

    axios.get('/get_region_data/', {
        params: {
            region: modelName
        }
    })
    .then(function (response) {
        console.log(response.data);
        document.getElementById('regionCell').textContent = regionName;
        document.getElementById('habitatsCell').textContent = response.data.habitats;
    })
    .catch(function (error) {
        console.log(error);
    });
}

// Légende
var legend = L.control({position: 'bottomright'});
legend.onAdd = function (carte) {
    var div = L.DomUtil.create('div', 'info legend');
    var labels = ["Bamako","Gao","Kayes","Kidal","Koulikoro","Mopti","Ségou","Sikasso","Timbuktu"];

    for (var i = 0; i < labels.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(labels[i]) + '"></i> ' +
            labels[i] + (labels[i + 1] ? '&ndash;' + labels[i + 1] + '<br>' : '+');
    }
    return div;
};
legend.addTo(map);

// Plugin de mesure de polygones
let measurePolygonControl = L.control.measurePolygon();
measurePolygonControl.addTo(map);

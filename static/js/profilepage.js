const copy = '© <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
const url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
const osm = L.tileLayer(url, { attribution: copy })
const map = L.map('map', { layers: [osm] , minZoom: 5})
map.locate().on('locationfound', e => map.setView(e.latlng, 4)).on('locationerror', () => map.setView([0, 0], 5))

// const profiles = JSON.parse(document.getElementById('markers-data').textContent)
// const features = L.geoJSON(profiles).bindPopup(layer => layer.feature.properties.homeAddress)
// const features = L.geoJSON(profiles, {
//     onEachFeature: function (feature, layer) {
//       layer.bindPopup(feature.properties.username +"</br>"+ feature.properties.homeAddress)
//    }
// })
// map.addLayer(features).fitBounds(features.getBounds())

async function load_markers() {
   const markers_url = `/api/profiles/?in_bbox=${map.getBounds().toBBoxString()}`
   const response = await fetch(markers_url)
   const geojson = await response.json()
   return geojson
}

function onClick(feature,e) {
     $.ajax({
          url: `/api/profiles/${feature.id}`,
          type: "GET"
        }).done(function (response) {
          // Construct the full URL with "id"
          document.location.href = `/profile/${feature.id}`;

        });
}

async function render_markers() {
  const markers = await load_markers()
  L.geoJSON(markers, {
      onEachFeature: function (feature, layer) {
        layer.bindTooltip(feature.properties.username +"</br>"+ feature.properties.homeAddress,{direction: 'top'})
        layer.on({
        click: onClick.bind(null,feature)
        });
     }
  }).addTo(map)
}

map.on('moveend', render_markers)

// map.fitWorld();

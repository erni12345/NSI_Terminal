let map;
let marker;
let current;


function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 2,
  });

  marker = new google.maps.Marker({
    position: new google.maps.LatLng(0,0),
    map: map
});
}


function setMarker(position){


  var data = position
  console.log("this is data ", current)
  marker.setPosition(new google.maps.LatLng(current[1], current[0]))
  console.log(marker)
}

async function getCoords() {
    let url="http://api.open-notify.org/iss-now.json"
    let coords
    await fetch(url)
    .then(response => response.json())
    .then(data => {

        coords = [parseFloat(data["iss_position"]["longitude"]), parseFloat(data["iss_position"]["latitude"])]
    })
    current = coords
}

async function updateMap(){
  await getCoords()
  setMarker()
}
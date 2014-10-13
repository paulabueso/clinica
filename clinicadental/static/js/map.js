function initialize() {
    var mapOptions = {
        zoom: 4,
        center: new google.maps.LatLng(37, -122)
    };
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    var myMarkers = [
        {
            lat: 38,
            lng: -122,
            name: 'place1'
        },
        {
            lat: 37,
            lng: -132,
            name: 'place2'
        },
        {
            lat: 39,
            lng: -132,
            name: 'place3'
        }
    ];

    for (i = 0; i < myMarkers.length; i++) {

        var contentString = '<p>hi</p>';
          var infowindow = new google.maps.InfoWindow({
        content: contentString
        });


        var newMarker= new google.maps.Marker({
            position: new google.maps.LatLng(myMarkers[i].lat, myMarkers[i].lng),
            map: map,
            title: myMarkers[i].name,
            icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 10
    }
        });
        (function (mark) {
           google.maps.event.addListener(mark, 'click', function () {
               map.setZoom(10);
               map.setCenter(mark.getPosition());
               infowindow.open(map,mark);
           });
       })(newMarker);

    }
}

google.maps.event.addDomListener(window, 'load', initialize);


function initialize() {}

function mapInitialize($el, location) {

  const mapMultiply = document.querySelector('.map-multiply');
  let zoomMultiply = 16;

  if (mapMultiply) {
    zoomMultiply = 10;
  }

  const mapStyle = [
    {
      'featureType': 'all',
      'elementType': 'labels.text.fill',
      'stylers': [
        {
          'saturation': 36,
        },
        {
          'color': '#000000',
        },
        {
          'lightness': 40,
        },
      ],
    },
    {
      'featureType': 'all',
      'elementType': 'labels.text.stroke',
      'stylers': [
        {
          'visibility': 'on',
        },
        {
          'color': '#000000',
        },
        {
          'lightness': 16,
        },
      ],
    },
    {
      'featureType': 'all',
      'elementType': 'labels.icon',
      'stylers': [
        {
          'visibility': 'off',
        },
      ],
    },
    {
      'featureType': 'administrative',
      'elementType': 'geometry.fill',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 20,
        },
      ],
    },
    {
      'featureType': 'administrative',
      'elementType': 'geometry.stroke',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 17,
        },
        {
          'weight': 1.2,
        },
      ],
    },
    {
      'featureType': 'landscape',
      'elementType': 'geometry',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 20,
        },
      ],
    },
    {
      'featureType': 'poi',
      'elementType': 'geometry',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 21,
        },
      ],
    },
    {
      'featureType': 'road.highway',
      'elementType': 'geometry.fill',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 17,
        },
      ],
    },
    {
      'featureType': 'road.highway',
      'elementType': 'geometry.stroke',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 29,
        },
        {
          'weight': 0.2,
        },
      ],
    },
    {
      'featureType': 'road.arterial',
      'elementType': 'geometry',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 18,
        },
      ],
    },
    {
      'featureType': 'road.local',
      'elementType': 'geometry',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 16,
        },
      ],
    },
    {
      'featureType': 'transit',
      'elementType': 'geometry',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 19,
        },
      ],
    },
    {
      'featureType': 'water',
      'elementType': 'geometry',
      'stylers': [
        {
          'color': '#000000',
        },
        {
          'lightness': 17,
        },
      ],
    },
  ];
  var mapOptions = {
    zoom: zoomMultiply,
    zoomControl: true,
    disableDoubleClickZoom: true,
    mapTypeControl: false,
    scaleControl: false,
    scrollwheel: false,
    panControl: false,
    streetViewControl: false,
    draggable: true,
    overviewMapControl: true,
    overviewMapControlOptions: {
      opened: false,
    },
    styles: mapStyle,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
  };
  const map = new google.maps.Map($el, mapOptions);

  const location_array = JSON.parse(location);

  for (var i in location_array) {
    var markerLatlng = new google.maps.LatLng(location_array[i][0],
        location_array[i][1]);
    map.setCenter(markerLatlng);
    var marker = new google.maps.Marker({
      map: map,
      //icon: '/img/map-marker.png',
      // icon: '/show/black-line-studio/img/map-marker.png',
      icon: '/static/img/map-marker.png',
      position: markerLatlng,
    });
  }
}

document.querySelectorAll('.contact-map').forEach(function(elem) {
  if (elem && window.google) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.intersectionRect.width * entry.intersectionRect.height / entry.boundingClientRect.width * entry.boundingClientRect.height >= 0.5) {
          mapInitialize(elem, elem.dataset.address);
          observer.unobserve(elem);
        }
      })
    });

    observer.observe(elem);
  }
});




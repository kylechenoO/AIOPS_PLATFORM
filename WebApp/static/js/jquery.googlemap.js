$(function() {
	'use strict';
	// CONTEXT MENU map
	var map;
	var map, infoWindow;
	var map, infoWindow;
	$(window).on("load", function(e) {
		var map;
		map = new GMaps({
			el: '#map',
			lat: -12.043333,
			lng: -77.028333,
			zoomControl: true,
			zoomControlOpt: {
				style: 'SMALL',
				position: 'TOP_LEFT'
			},
			panControl: false,
			streetViewControl: false,
			mapTypeControl: false,
			overviewMapControl: false
		});
		map = new GMaps({
			el: '#simple-map',
			lat: -12.043333,
			lng: -77.028333
		});
		map.setContextMenu({
			control: 'map',
			options: [{
				title: 'Add marker',
				name: 'add_marker',
				action: function(e) {
					console.log(e.latLng.lat());
					console.log(e.latLng.lng());
					this.addMarker({
						lat: e.latLng.lat(),
						lng: e.latLng.lng(),
						title: 'New marker'
					});
					this.hideContextMenu();
				}
			}, {
				title: 'Center here',
				name: 'center_here',
				action: function(e) {
					this.setCenter(e.latLng.lat(), e.latLng.lng());
				}
			}]
		});
		map.setContextMenu({
			control: 'marker',
			options: [{
				title: 'Center here',
				name: 'center_here',
				action: function(e) {
					this.setCenter(e.latLng.lat(), e.latLng.lng());
				}
			}]
		});
		map = new GMaps({
			el: '#map1',
			lat: -12.043333,
			lng: -77.028333
		});
		map.addMarker({
			lat: -12.043333,
			lng: -77.03,
			title: 'Lima',
			details: {
				database_id: 42,
				author: 'HPNeo'
			},
			click: function(e) {
				if (console.log) console.log(e);
				alert('You clicked in this marker');
			},
			mouseover: function(e) {
				if (console.log) console.log(e);
			}
		});
		map.addMarker({
			lat: -12.042,
			lng: -77.028333,
			title: 'Marker with InfoWindow',
			infoWindow: {
				content: '<p>HTML Content</p>'
			}
		});
		infoWindow = new google.maps.InfoWindow({});
		map = new GMaps({
			el: '#map2',
			zoom: 12,
			lat: 40.65,
			lng: -73.95
		});
		map.loadFromKML({
			url: 'http://api.flickr.com/services/feeds/geo/?g=322338@N20&lang=en-us&format=feed-georss',
			suppressInfoWindows: true,
			events: {
			  click: function(point){
				infoWindow.setContent(point.featureData.infoWindowHtml);
				infoWindow.setPosition(point.latLng);
				infoWindow.open(map.map);
			  }
			}
		});
		var map = new GMaps({
			el: "#map3",
			lat: 41.895465,
			lng: 12.482324,
			zoom: 5,
			zoomControl: true,
			zoomControlOpt: {
				style: "SMALL",
				position: "TOP_LEFT"
			},
			panControl: true,
			streetViewControl: false,
			mapTypeControl: false,
			overviewMapControl: false
		});
		var styles = [{
			stylers: [{
				hue: "#00ffe6"
			}, {
				saturation: -20
			}]
		}, {
			featureType: "road",
			elementType: "geometry",
			stylers: [{
				lightness: 100
			}, {
				visibility: "simplified"
			}]
		}, {
			featureType: "road",
			elementType: "labels",
			stylers: [{
				visibility: "off"
			}]
		}];
		map.addStyle({
			styledMapName: "Styled Map",
			styles: styles,
			mapTypeId: "map_style"
		});
		map.setStyle("map_style");
		map = new GMaps({
			el: '#map4',
			lat: -12.043333,
			lng: -77.028333
		});
		map.drawRoute({
			origin: [-12.044012922866312, -77.02470665341184],
			destination: [-12.090814532191756, -77.02271108990476],
			travelMode: 'driving',
			strokeColor: '#131540',
			strokeOpacity: 0.6,
			strokeWeight: 6
		});
	});
});
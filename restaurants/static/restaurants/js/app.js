function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(lookupAddress, locationError, {timeout: 10000});
    } else {
        alert("Geolocation is not supported by this browser.")
    }
};

function showAddress(address) {
    console.log(address);
    if (!$('#locator').val()) {
        $('#locator').val(address);
    };
};

function locationError(err) {
    console.log(err);
};

function lookupAddress(position) {
	var geocoder = new google.maps.Geocoder();
    var latlng = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
    };
    geocoder.geocode({
        'location': latlng
    }, function(results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            if (results[1]) {
                showAddress(results[1].formatted_address);
            } else {
                alert('No results found');
            }
        } else {
            alert('Geocoder failed due to: ' + status);
        }
    });
}

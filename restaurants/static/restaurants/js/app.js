function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(lookupAddress);
    } else {
        alert("Geolocation is not supported by this browser.")
    }
};

function showAddress(address) {
    $('#locator').val(address)
    console.log(address)
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

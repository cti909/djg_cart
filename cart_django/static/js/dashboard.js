$.ajax({
    url: '/dashboard/',
    dataType: 'json',
    success: function(data) {
        console.log(data)
    },
    error: function(data) {
        console.log("asd")
    }
});

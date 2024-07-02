

$(function(){
    var elem = $('.ajax');
    $.ajax({
    url: 'http://127.0.0.1:8000/gen/photo/c00ea533-99bd-4229-af18-b771d3a06f7d/',
    type: 'GET',
    dataType: 'json',
    success: function(response){
        $('.ajax').before(response.data.data);
        console.log(response.status);
    },
    error: function(x,e) {
    if (x.status==0) {
        alert('You are offline!!\n Please Check Your Network.');
    } else if(x.status==404) {
        alert('Requested URL not found.');
    } else if(x.status==500) {
        alert('Internel Server Error.');
    } else if(e=='parsererror') {
        alert('Error.\nParsing JSON Request failed.');
    } else if(e=='timeout'){
        alert('Request Time out.');
    } else {
        alert('Unknow Error.\n'+x.responseText);
    }
}
    });
});


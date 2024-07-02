$(function(){
function MakeRequest (urlData){
        $.ajax({
            url: urlData,
            type: 'get',
            success: function(response){
                if (response.state === "SUCCESS"){
                    var img = $('.imageshort-icon')
                    img.fadeOut(1000)
                    setTimeout(changeAttr, 1000, img, 'src', urlPhoto)

                } else {
                    setTimeout(Error, 500);
                }
            }
        })
    };

function changeAttr (obj, attr_key, value) {
    obj.attr(attr_key, value);
    return obj.fadeIn(1000)
}
function alertTest(obj) {
    alert(obj)
    return True
}
function changeAttrNoFade (obj, attr_key, value) {
    obj.attr(attr_key, value);
}
});
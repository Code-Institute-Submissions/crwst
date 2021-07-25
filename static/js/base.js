/* 
Zoom transition code adapted from (https://stackoverflow.com/questions/33811041/
javascript-zoom-in-on-mouseover-without-jquery-or-plugins) 
*/

$(document).ready(function() {
    /* Zoom in effect */
    $(".zoomIn").hover(function() {
        $(".zoomIn").addClass('transition');

    }, function() {
        $(".zoomIn").removeClass('transition');
    });
    /* Toasts */
    $('.toast').toast('show');
});
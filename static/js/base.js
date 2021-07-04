
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
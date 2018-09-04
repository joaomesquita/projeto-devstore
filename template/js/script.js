$(window).scroll(function() {
    if ($(document).scrollTop() > 100) {
        $('.navbar-content').addClass('affix');
    } else {
        $('.navbar-content').removeClass('affix');
    }
});
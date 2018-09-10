// Scroll fixed
$(window).scroll(function() {
    if ($(document).scrollTop() > 50) {
        $('.menu').addClass('affix');
    } else {
        $('.menu').removeClass('affix');
    }
});

// Dropdown hover
$(".dropdown").hover(
    function() {
        $('.dropdown-menu', this).fadeIn(100);
    },
    function() {
        $('.dropdown-menu', this).fadeOut(100);
    }
);

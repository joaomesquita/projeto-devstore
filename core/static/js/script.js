// Scroll fixed
$(window).scroll(function() {
    if ($(document).scrollTop() > 50) {
        $('.menu').addClass('affix');
    } else {
        $('.menu').removeClass('affix');
    }
});

// Dropdown hover
$('.dropdown').hover(
    function() {
        $('.dropdown-menu', this).fadeIn(100);
    },
    function() {
        $('.dropdown-menu', this).fadeOut(100);
    }
);

// Number snippet
$(document).ready(function(){
    $('.btn-plus').click(function(){
        var quantity = parseInt($('#quantity').val());
        $('#quantity').val(quantity + 1);
    });
        $('.btn-minus').click(function(){
        var quantity = parseInt($('#quantity').val());
        if(quantity > 0){
            $('#quantity').val(quantity - 1);
        }
    });
});
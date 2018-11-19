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

// ALert
window.setTimeout(function() {
    $(".messages").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 4000);

// Mask inputs
$(document).ready(function(){
    $('.date').mask('00/00/0000');
    $('.phone_with_ddd').mask('(00) 00000-0000');
    $('.cpf').mask('000.000.000-00', {reverse: true});
    $('.cep').mask('00000-000');
});
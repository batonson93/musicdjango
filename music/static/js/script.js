$(document).ready(function() {

    if ($(window).width() > 800) {
       $(document).ajaxComplete( function (){
                var a = $('.post img').width();
                 $('.post img').css('height', a / 1.74 + 'px');
       });
        var a = $('.post img').width();
        var b = $('.other-posts .post img').width();
        $('.post img').css('height', a / 1.74 + 'px');
        $('.post video').css('height', a / 1.74 + 'px');
        $('.other-post-info').css('height', b / 1.74 + 'px');
        $('.other-posts .post img').css('height', b / 1.74 + 'px');
    }

    var videoHeight = ($(".video").width() * 0.5625) + 'px';
    $(".video").css('height', videoHeight);

    var c = $('.single img').width();
    var d = $('.album img').width();
    var e = $('.shop-item img').width();
    $('.single img').css('height', c + 'px');
    $('.album img').css('height', d + 'px');
    $('.listen-pad').css('height', d + 'px');
    $('.shop-item img').css('height', e + 'px');

    $('.listen').click(function() {
        if ($(this).parent().parent().children(".listen-pad").hasClass('listen-pad-show')) {
            $(this).parent().parent().children(".listen-pad").removeClass('listen-pad-show');
            $(this).html('Listen');
        } else {
            $(this).parent().parent().children(".listen-pad").addClass('listen-pad-show');
            $(this).html('Close');
        }
    });

    $('.close').click(function() {
        $(this).parent().removeClass('listen-pad-show');
    });

    if ($('html').hasClass('mobile') || $('html').hasClass('tablet') || ($(window).width() <= 800)) {
        $('.other-post-info').css('display', 'none');
        $('.other-posts .post').addClass('post-mobile');
        $('body').css('background-size', '100%');
    };


    $(window).bind('resize', function(event) {
        var videoHeight = ($(".video").width() * 0.5625) + 'px';
        $(".video").css('height', videoHeight);
        if (!($('html').hasClass('mobile') || $('html').hasClass('tablet'))) {
            if ($(window).width() <= 800) {
                $('.other-post-info').css('display', 'none');
                $('.other-posts .post').addClass('post-mobile');
                $('body').css('background-size', '100%');
            } else {
                $('.other-post-info').css('display', 'block');
                $('.other-posts .post').removeClass('post-mobile');
                $('body').css('background-size', 'auto');
                $('.mobile-nav').removeClass('mobile-nav-open');
            }
        } else {
            if ($(window).width() > 800) {
                $('.mobile-nav').removeClass('mobile-nav-open');
            }
        }
    });

    $(window).bind('resize', function(event) {
        var a = $('.post img').width();
        var b = $('.other-posts .post img').width();
        var c = $('.single img').width();
        var d = $('.album img').width();
        var e = $('.shop-item img').width();
        $('.post img').css('height', a / 1.74 + 'px');
        $('.post video').css('height', a / 1.74 + 'px');
        $('.other-posts .post img').css('height', b / 1.74 + 'px');
        $('.other-post-info').css('height', b / 1.74 + 'px');
        $('.single img').css('height', c + 'px');
        $('.album img').css('height', d + 'px');
        $('.listen-pad').css('height', d + 'px');
        $('.shop-item img').css('height', e + 'px');
    });

    if ($('html').hasClass('mobile') || $('html').hasClass('tablet')) {
        if ($('.other-videos').hasClass('other-videos-mobile')) {
            $('.other-videos').removeClass('other-videos-mobile');
        } else {
            $('.other-videos').addClass('other-videos-mobile');
        }
        $('body, button, h3, input').css('font-weight', 'bold');
    }

    $(document).click(function(e) {
        if (!($('.hamburger').is(e.target)) && !($('.main-header .container').is(e.target)) && !($('.mobile-nav').is(e.target)) && $('.mobile-nav').has(e.target).length === 0) {
            $('.mobile-nav').removeClass('mobile-nav-open');
        } else if ($('.hamburger').is(e.target)) {
            if ($('.mobile-nav').hasClass('mobile-nav-open')) {
                $('.mobile-nav').removeClass('mobile-nav-open');
            } else {
                $('.mobile-nav').addClass('mobile-nav-open');
            }
        }
    });

});

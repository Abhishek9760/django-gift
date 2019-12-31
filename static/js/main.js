$('document').ready(function () {
    if ($('.text-slider').length == 1) {
        var typed_strings = $('.text-slider-items').text();
        var typed = new Typed('.text-slider', {
            strings: typed_strings.split(';'),
            typeSpeed: 100,
            loop: false,
            backDelay: 1100,
            backSpeed: 30,
            startDelay: 2000,
            smartBackspace: true,
            // shuffle: true
            // fadeOut: true
            // cursorChar: '~'
            // showCursor: false,
            // onBegin: function(self) { preety('onBegin') },
            // onStart: function () {
            // 	console.log('onBegin')
            // },
            onComplete: function onComplete(self) {
                $('.main-content').html("<p class=\"pt-3\"><a class=\"btn btn-outline-success btn js-scroll px-4\" href='thank-you/' role=\"button\">Yes❤</a></p>")
            },

        });

    }


    var urls = [
        'static/img/amruta/IMG-20190929-WA0016.jpg',
        'static/img/amruta/IMG-20191002-WA0017.jpg',
        'static/img/amruta/IMG-20191004-WA0051.jpg',
        'static/img/amruta/IMG-20191025-WA0014.jpg',
        'static/img/amruta/IMG-20191027-WA0022.jpg',
        'static/img/amruta/IMG-20191027-WA0023.jpg',
        'static/img/amruta/IMG-20191029-WA0014.jpg',
        'static/img/amruta/IMG-20191127-WA0021.jpg',
        'static/img/amruta/IMG-20191127-WA0022.jpg',
        'static/img/amruta/IMG-20191127-WA0023.jpg',
        'static/img/amruta/IMG-20191127-WA0024.jpg',
        'static/img/amruta/IMG-20191127-WA0025.jpg',
        'static/img/amruta/IMG-20191127-WA0026.jpg',
        'static/img/amruta/IMG-20191127-WA0027.jpg',
        'static/img/amruta/IMG-20191202-WA0009.jpg',
        'static/img/amruta/IMG-20191207-WA0001.jpg',
        'static/img/amruta/IMG-bhb.jpg',
        'static/img/amruta/IMG_20191108_201628_904.jpg'
    ];

    var cout = 1;
    $('#home-pics').css('background-image', 'url("' + urls[0] + '")');
    setInterval(function () {
        $('#home-pics').css('background-image', 'url("' + urls[cout] + '")');
        cout == urls.length - 1 ? cout = 0 : cout++;
    }, 5000);
});


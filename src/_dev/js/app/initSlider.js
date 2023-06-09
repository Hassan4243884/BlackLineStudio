import {tns} from 'tiny-slider/src/tiny-slider';
// import 'instafeed.js/instafeed';
import GrayScaleFix from '../app_vendors/grayscale';
import Vivus from 'vivus/dist/vivus';
import Swiper from 'swiper/dist/js/swiper';
import lozad from 'lozad';


var mainSlider = document.querySelector('.main-slider');
if (mainSlider) {
    const slider = tns ({
        "container": '.main-slider',
        "slideBy": 'page',
        "controls": true,
        "autoplay": true,
        "speed": 1000,
        lazyload: true,
        "controlsText": ['', ''],
        onInit: instance => {
            instance.container.classList.remove('_fix')
        }
    });
}

var artSlider = document.querySelector('.art-slider');
if (artSlider) {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 2,
        spaceBetween: 10,
        loop: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        lazy: {
            loadPrevNext: true,
            loadPrevNextAmount: 2
        }
    });
}

var galleryCarousel = document.querySelector('.gallery');
if (galleryCarousel) {
    const slider = tns ({
        "container": '.gallery',
        "items": 2,
        "slideBy": 1,
        "controls": false,
        "controlsText": ['', ''],
        "loop": false,
        "rewind": true,
        "autoplay": true,
        lazyload: true,
        "responsive": {
            "460": {
                "autoplay": false,
            },
            "740": {
                "items": 3,
            },
            "920": {
                "items": 4,
            },
            "1280": {
                "items": 8,
            },
        },
    });
}

var innerGalleryCarousel = document.querySelector('.js-inner-gallery');
if (innerGalleryCarousel) {
    const slider = tns ({
        "container": '.gallery',
        "items": 2,
        "slideBy": 1,
        "controls": false,
        "controlsText": ['', ''],
        "loop": false,
        "rewind": true,
        lazyload: true,
        "responsive": {
            "480": {
                "items": 3,
                "controls": true,
            },
            "920": {
                "items": 3,
            },
            "1080": {
                "items": 4,
            },
        },
    });
}

var servicesCarousel = document.querySelector('.services-carousel');

if (servicesCarousel) {
    const slider = tns ({
        "container": '.services-carousel',
        "items": 1,
        "gutter": 32,
        "controls": true,
        "edgePadding": 10,
        "autoHeight": true,
        "controlsText": ['', ''],
        "responsive": {
            "480": {
                "edgePadding": 50,
            },
            "600": {
                "edgePadding": 150,
            },
            "740": {
                "autoHeight": false,
            },
            "800": {
                "items": 2
            },
            "1120": {
                "items": 3
            }
        },
        onInit: function () {
            const animateIcons = document.querySelector('.js-icons-animate');

            if (animateIcons) {
                var els= document.getElementsByClassName("js-svg-animate");

                for (var i = els.length - 1; i >= 0; i--) {
                    new Vivus(els[i], {
                            duration: 50, type: 'sync'
                        }
                    );
                }
            }
        }
    });
}


var progressCarousel = document.querySelector('.progress-carousel');
if (progressCarousel) {
    const slider = tns ({
        "container": '.progress-carousel',
        "items": 1,
        "gutter": 32,
        "controls": true,
        "loop": false,
        "edgePadding": 10,
        "controlsText": ['', ''],
        "responsive": {
            "480": {
                "items": 2
            },
            "740": {
                "items": 3
            },
            "960": {
                "items": 4
            }
        },
        onInit: function (instance) {
            instance.container.classList.remove('_fix');
        }
    });
}

var galleries = document.querySelectorAll('.js-artists'), i;
for (i = 0; i < galleries.length; ++i) {
    const team_slider = tns ({
        "container": galleries[i],
        "controls": true,
        "items": 1,
        lazyload: true,
        "controlsText": ['', ''],
        "responsive": {
            "640": {
                "items": 2
            },
            "860": {
                "items": 3,
            }
        },
    });
}

var instagramCarousel = document.querySelector('.instagram-posts');
if (instagramCarousel) {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.intersectionRect.width * entry.intersectionRect.height / entry.boundingClientRect.width * entry.boundingClientRect.height >= 0.5) {
                var Instafeed = require("instafeed.js");
                var target = document.querySelector('.instagram-posts');

                var feed = new Instafeed({
                    get: 'user',
                    target: target,
                    userId: '220269150',
                    accessToken: '220269150.1677ed0.105ede89ad4445ddb61f49c168674e0c',
                    useHttp: "true",
                    resolution: "standard_resolution",
                    template:
                        '<div class="instagram-posts__slide grayscale-wr">' +
                        '<a href="{{link}}" target="_blank" class="instagram-posts__link grayscale" id="{{id}}" style="background-image: url({{image}})">' +
                        '</a>' +
                        '</div>',

                    after: function() {
                        const slider = tns ({
                            "container": '.instagram-posts',
                            "controls": true,
                            "items": 1,
                            "controlsText": ['', ''],
                            "autoplay": true,
                            "responsive": {
                                "480": {
                                    "autoplay": false,
                                    "items": 2
                                },
                                "740": {
                                    "items": 3
                                },
                                "1024": {
                                    "items": 5,
                                },
                                "1180": {
                                    "items": 7,
                                }
                            }
                        });
                    }
                });
                feed.run();
                observer.unobserve(instagramCarousel);
            }
        })
    });

    observer.observe(instagramCarousel);
}

var testimonials = document.querySelector('.testimonials');
if (testimonials) {
    const slider = tns ({
        "container": '.testimonials',
        "controls": true,
        "items": 1,
        "controlsText": ['', ''],
        "autoplay": true,
        "responsive": {
            "480": {
                "autoplay": false,
            },
        },
    });
}


var innerSlider = document.querySelector('.inner-slider');
if (innerSlider) {
    const slider = tns ({
        "container": innerSlider,
        "controls": true,
        "items": 1,
        "controlsText": ['', ''],
        "autoplay": true,
        "lazyload": true,
        "responsive": {
            "480": {
                "autoplay": true,
            },
        },
    });
}






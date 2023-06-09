var topGroup = document.querySelector('.top-group');

if ( topGroup ) {
    function mainHeadTopIndent() {
        var headerHeight = 0;
        var header = document.querySelector('.header');
        if(header)
        {
            headerHeight = header.clientHeight;
        }

        var mainHead = document.querySelector('.main-head');
        mainHead.style.paddingTop = headerHeight + 16 + 'px';
    }

    function mainSlideHeight() {
        var  mainHead = document.querySelector('.main-head');
        var mainHeadHeight = 0;
        if(mainHead)
            mainHeadHeight = mainHead.clientHeight;

        //var mainSliderSlide = document.querySelector('.main-slider__slide');
        var mainSliderWrapper = document.querySelector('.main-slider-wrapper');
        var mainSlider = document.querySelector('.main-slider');
        //mainSliderSlide.style.height = mainHeadHeight + 'px';
        mainSliderWrapper.style.height = mainHeadHeight + 'px';
        mainSlider.style.height = mainHeadHeight + 'px';
    }

    mainHeadTopIndent();
    mainSlideHeight();

    window.addEventListener('load', function () {
        mainHeadTopIndent();
        mainSlideHeight();
    });

    window.addEventListener('resize', function () {
        mainHeadTopIndent();
        mainSlideHeight();
    });
}

var innerBanner = document.querySelector('.inner-banner');

if (innerBanner) {
    function innerBannerIndent() {
        var headerHeight = 0;
        var header = document.querySelector('.header');
        if(header)
        {
            headerHeight = header.clientHeight;
        }

        var innerBanner = document.querySelector('.inner-banner');
        innerBanner.style.paddingTop = headerHeight + 16 + 'px';
    }

    innerBannerIndent();
}








const headerLogo = document.querySelector('.header__logo');
const jsSecondSection = document.querySelector('.js-second');

if (jsSecondSection) {
    function hLogoAnimate() {
        window.addEventListener('resize', function () {
            if ( screen.width <= 560 ) {
                headerLogo.classList.add('hide');
            } else {
                headerLogo.classList.remove('hide');
            }
        });
    }

    function logoScrollAnimate() {
        const secondSectionPos = jsSecondSection.offsetTop;

        headerLogo.classList.add('hide');

        window.addEventListener('scroll', function () {
            var windowPos = window.pageYOffset;

            if ( windowPos >= secondSectionPos / 2 ) {
                headerLogo.classList.remove('hide');
            } else {
                headerLogo.classList.add('hide');
            }
        });
    }

    hLogoAnimate();

    if ( screen.width <= 560 ) {
        logoScrollAnimate();
    }
}









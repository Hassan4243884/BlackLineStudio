import Vivus from 'vivus/dist/vivus';

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




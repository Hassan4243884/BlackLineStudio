import GLightbox from 'glightbox/dist/js/glightbox'

var gallery = document.querySelector('.gallery-wrapper');

if ( gallery ) {
    var myLightbox = GLightbox({
        'selector': 'glightbox',
        'moreLength': 300,
        'loopAtEnd': false,
    });
}




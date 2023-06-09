const accordion = document.querySelector('.accordion');

if (accordion) {

    var acc = document.getElementsByClassName("js-accordion-title");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.closest('.accordion__container').classList.toggle("open");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    }

}

function mainAccordionInit() {
    var mainAccordionSection = document.querySelectorAll('.main-accordion__section');
    var mainAccordionButton = document.querySelectorAll('.js-ma-title');

    mainAccordionButton.forEach(function (el) {
        el.addEventListener('click', function () {

            if ( this.parentNode.classList.contains('active') ) {
                this.parentNode.classList.remove('active');
            } else {
                this.parentNode.classList.add('active');
            }
        });
    });
}

mainAccordionInit();






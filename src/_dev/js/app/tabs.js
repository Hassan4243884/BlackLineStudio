const tabBtn = document.querySelectorAll('.js-tab-btn');
const tabContainer = document.querySelectorAll('.main-tabs__section');

function Tabs() {

    var bindAll = function() {
        var menuElements = document.querySelectorAll('[data-tab]');
        for(var i = 0; i < menuElements.length ; i++) {
            menuElements[i].addEventListener('click', change, false);
        }
    };

    var clear = function() {
        var menuElements = document.querySelectorAll('[data-tab]');
        for(var i = 0; i < menuElements.length ; i++) {
            menuElements[i].classList.remove('active');
            var id = menuElements[i].getAttribute('data-tab');
            document.getElementById(id).classList.remove('active');
        }
    };

    var change = function(e) {
        clear();
        e.target.classList.add('active');
        var id = e.currentTarget.getAttribute('data-tab');
        document.getElementById(id).classList.add('active');
    };

    bindAll();

}

var connectTabs = new Tabs();

const accordionBtn = document.querySelectorAll('.js-accordion-btn');
const accordionContainer = document.querySelectorAll('.js-info-accorfion-section');
const windowWidth = window.innerWidth;

function informationAccordion() {
    accordionBtn.forEach(function (el) {
        el.addEventListener('click', function () {

            if ( this.parentNode.classList.contains('active') ) {
                this.parentNode.classList.remove('active');
            } else {
                this.parentNode.classList.add('active');
            }

            // accordionContainer.forEach(function (el) {
            //     el.classList.remove('active');
            // });


        })
    });
}

informationAccordion();











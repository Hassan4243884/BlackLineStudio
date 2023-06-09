const dropdownTrigger = document.querySelectorAll('.js-trigger-dropdown');

dropdownTrigger.forEach(function (el) {
    el.addEventListener('click', function (event) {
        event.preventDefault();
        if (this.closest('.oc-menu__item').classList.contains('active')) {
            this.closest('.oc-menu__item').classList.remove('active');
        } else {
            this.closest('.oc-menu__item').classList.add('active');
        }
    })
});



function fieldChange() {
    var formField = document.querySelectorAll('.form-section__field');
    var formSelect = document.querySelectorAll('.form-section__select');
    var placeholder_tmp;

    formField.forEach(function (el) {

        el.addEventListener('focus', function () {
            placeholder_tmp = el.getAttribute('placeholder');
            el.setAttribute("placeholder", "");

            el.parentNode.classList.add('active');
        });

        el.addEventListener('blur', function () {
            el.setAttribute("placeholder", placeholder_tmp);
            el.parentNode.classList.remove('active');

            if (el.value.length != 0) {
                el.parentNode.classList.add('active');
            }
        });
    });

    formSelect.forEach(function (el) {

        el.addEventListener('change', function () {
            el.parentNode.classList.add('active');
        });
    });
}

fieldChange();







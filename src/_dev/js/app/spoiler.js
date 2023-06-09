const spoiler = document.querySelectorAll('.spoiler-container');
const spoilerTop = document.querySelectorAll('.spoiler-container_top');
const spoilerTest = document.querySelectorAll('.spoiler-test');
const spoilerBtn = document.querySelectorAll('.spoiler-btn');
const spoilerOpen = document.querySelector('.js-spoiler-open');
const spoilerClose = document.querySelector('.js-spoiler-close');
const spoilerContentTrigger = document.querySelectorAll('.js-spoiler-trigger');

if (spoiler) {
    spoilerBtn.forEach(function (el) {
        el.addEventListener('click', function (event) {
            var spoilerContainer = event.target.closest('.spoiler-container').querySelector('.js-spoiler');
            spoilerContainer.classList.toggle('hidden');

            if (this.closest('.spoiler-container').classList.contains('active')) {
                this.closest('.spoiler-container').classList.remove('active');
                event.target.innerText = 'More details';
            } else {
                this.closest('.spoiler-container').classList.add('active');
                event.target.innerText = 'Minimize';
            }
        })
    });
}

if (spoilerTop && spoilerOpen && spoilerClose) {
    spoilerOpen.addEventListener('click', function () {
        this.closest('.spoiler-container').classList.add('active');
    });

    spoilerClose.addEventListener('click', function () {
        this.closest('.spoiler-container').classList.remove('active');
    });
}

console.log(spoilerContentTrigger);

spoilerContentTrigger.forEach(function (el) {
    el.addEventListener('click', function () {
        if (el.closest('.spoiler-container').classList.contains('is-open')) {
            el.closest('.spoiler-container').classList.remove('is-open');
            el.closest('.spoiler-container').querySelector('.spoiler').classList.add('hidden');
        } else {
            el.closest('.spoiler-container').classList.add('is-open');
            el.closest('.spoiler-container').querySelector('.spoiler').classList.remove('hidden');
        }
    })
});





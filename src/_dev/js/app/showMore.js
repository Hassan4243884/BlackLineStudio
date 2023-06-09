import {tns} from "tiny-slider/src/tiny-slider";

document.querySelectorAll('.js-show_more').forEach(el => {
    el.addEventListener('click', () => {
        document.querySelectorAll(`${el.dataset.target}`).forEach( target =>{
            target.classList.remove('_hidden');
        });
        el.style.display = 'none';
    })
});

const scrollBtn = document.querySelectorAll('.jsScrollTo');
const whereScroll = document.querySelector('#form');

if (scrollBtn && whereScroll) {
    var whereScrollOffset = whereScroll.offsetTop;
    const preFooter = document.querySelector('.pre-footer');
    const preFooterHeight = preFooter.clientHeight;

    scrollBtn.forEach(function (el) {
        el.addEventListener('click', function () {
            if (window.width <= 740) {
                window.scrollTo(0, whereScrollOffset + preFooterHeight - 100);
            } else {
                window.scrollTo(0, whereScrollOffset + preFooterHeight/2);
            }
        });
    });
}


//var jsBtn = document.querySelectorAll('.js-btn');
//var sectionTarget = document.querySelectorAll('.js-target');
//
//jsBtn.forEach(function (el) {
//    console.log(el.dataset.scroll);
//
//    el.addEventListener('click', function () {
//        console.log(jsBtnScroll);
//    })
//});








window.onscroll = function() {myFunction()};

const header = document.getElementById("header");
const navbarYPos = header.getBoundingClientRect();
const sticky = header.offsetTop;

function myFunction() {

    if ( sticky.top != 0 ) {
        header.classList.add("sticky-header");
    }
    if (window.pageYOffset >= sticky + 1) {
        header.classList.add("is-stuck");
    } else {
        header.classList.remove("is-stuck");
    }
}

function headerHeight() {
    var windowHeight = document.getElementById("header").height;
    header.setAttribute("style", "height: " + windowHeight + "px");
}

window.addEventListener('load', function () {
    myFunction();
});

window.addEventListener('resize', function () {
    setTimeout(function () {
        headerHeight();
    }, 100);
});



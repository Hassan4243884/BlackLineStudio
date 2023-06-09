function columnMaxHeight() {
    var mainDivs = document.getElementsByClassName("js-max-height");
    var maxHeight = 0;
    for (var i = 0; i < mainDivs.length; ++i) {
        if (maxHeight < mainDivs[i].clientHeight) {
            maxHeight = mainDivs[i].clientHeight;
        }
    }
    for (var i = 0; i < mainDivs.length; ++i) {
        mainDivs[i].style.height = maxHeight + 60 + "px";
    }
}

columnMaxHeight();

window.addEventListener('load', function () {
    columnMaxHeight();
});

// window.addEventListener('resize', function () {
//     columnMaxHeight();
// });



const offCanvas = document.querySelector('.off-canvas');
const openBtn = document.querySelector('.off-canvas-open');
const closeBtn = document.querySelector('.close-button');
const sidebar = document.querySelector('.off-canvas__sidebar');
const container = document.querySelector('.off-canvas__container');

function ocOpen() {

    openBtn.addEventListener('click', function () {

        let createOverlay = document.createElement('div');
        createOverlay.className = 'overlay';
        offCanvas.classList.add('active');

        if ( document.querySelector('.overlay') ) {
            return false;
        } else {
            container.appendChild(createOverlay);
            createOverlay.addEventListener('click', function () {
                offCanvas.classList.remove('active')
            });
        }

    });

    closeBtn.addEventListener('click', function () {
        offCanvas.classList.remove('active')
    });

}

ocOpen();



import './app/forEach';
import './app/closest';
import svg4everybody from 'svg4everybody';
import 'intersection-observer';
import lozad from 'lozad';

svg4everybody();

const lozadObserver = lozad('.lozad', {
  loaded: el => {
    if (el.getAttribute('data-src') || el.getAttribute('data-srcset')) {
      el.onload = () => {
        el.classList.add('fade');
      };
    }
  },
});

const lozadObserver1 = lozad('.lozadGray', {
  loaded: el => {
    if (el.getAttribute('data-src') || el.getAttribute('data-srcset')) {
      el.onload = () => {
        GrayScaleFix();
      };
    }
  },
});

lozadObserver.observe();
lozadObserver1.observe();

import './app/stickyInit';
import './app/headerLogoAnimate';
import './app/counter-animate';
import './app/svgAnimate';
import './app/initSlider';
import './app/formFieldFunc';
import './app/grayscale';
import './app/headSizes';
import './app/accordionInit';
import './app/offCanvasInit';
import './app/galleryItin';
import './app/spoiler';
import './app/columnHeight';
import './app/showMore';
//import './app/instafeed';
import './app/scrollToPreFooter';
import './app/tabs';
import './app/map';
import './app/menuDropdown';
import './app/scrollTo';


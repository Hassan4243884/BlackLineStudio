import gulp from 'gulp';

import {styles, stylesDjango, stylesWatch} from './compass';
import {appJs, appJsWatch} from './scripts';
import {svgSprite, svgSpriteWatch} from './sprite-svg/sprite-svg';

gulp.task('default', gulp.parallel(styles, stylesDjango, stylesWatch, appJs, appJsWatch, svgSprite, svgSpriteWatch));

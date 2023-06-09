import gulp from 'gulp';
import responsive from 'gulp-responsive';
import config from '../config';

export const images = () => (
    gulp.src(config.src.imgSource + '/**/*.{jpg,png}').
        pipe(responsive({
          '**/*.png': [
            {
              quality: 80,
              progressive: false,
              compressionLevel: 7,
            }],
          '**/*.jpg': [
            {
              quality: 80,
              progressive: true,
            }],
        })).
        pipe(gulp.dest(config.src.img))
);

gulp.task('images', images);

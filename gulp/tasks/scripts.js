import gulp from 'gulp';
import uglify from 'gulp-uglify';
import webpack from 'webpack';
import gulpWebpack from 'webpack-stream';
import webpackConfig from '../../config/webpack.config';
import config from '../config';

export const appJs = () => (
    gulp.src(config.src.js + '/main.js').
        pipe(gulpWebpack(webpackConfig), webpack).
        pipe(gulp.dest(config.src.assets + '/js')).
        pipe(uglify()).
        pipe(gulp.dest(config.src.assets + '/js')).
        pipe(gulp.dest(config.src.djangoAssets + '/js'))
);

export const appJsWatch = () => (
    gulp.watch(config.src.js + '/**/*.js', appJs)
);

gulp.task('js:app', appJs);
gulp.task('js:app:watch', appJsWatch);
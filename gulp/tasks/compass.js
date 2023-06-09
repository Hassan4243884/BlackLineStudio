import gulp from 'gulp';
import compass from 'gulp-compass';
import autoprefixer from 'gulp-autoprefixer';
import config from '../config';

export function styles() {
  return gulp.src(config.src.scss + '/*.scss').
      pipe(compass({
        config_file: './config.rb',
        css: config.src.assets + '/css',
        sass: config.src.scss,
        import_path: './node_modules',
        environment: 'development',
      })).
      on('error', function(error) {
        console.log(error);
        this.emit('end');
      }).
      pipe(autoprefixer(['last 2 versions', 'ie >= 9', 'iOS >= 7'])).
      pipe(gulp.dest(config.src.assets + '/css')).
      on('end', function() {
        gulp.src(config.src.assets + '/css/start.css').pipe(
            gulp.dest(config.src.includes + '/css'),
        );
      });
}

export function stylesDjango() {
  return gulp.src(config.src.scss + '/*.scss').
      pipe(compass({
        config_file: './config.rb',
        css: config.src.djangoAssets + '/css',
        sass: config.src.scss,
        import_path: './node_modules',
        environment: 'production',
      })).
      on('error', function(error) {
        console.log(error);
        this.emit('end');
      }).
      pipe(autoprefixer(['last 2 versions', 'ie >= 9', 'iOS >= 7'])).
      pipe(gulp.dest(config.src.djangoAssets + '/css')).
      on('end', function() {
        gulp.src(config.src.djangoAssets + '/css/start.css').pipe(
            gulp.dest(config.src.djangoTemplates),
        );
      });
}

export function stylesWatch() {
  gulp.watch(config.src.scss + '/**/*.scss',
      gulp.parallel(styles, stylesDjango));
}

gulp.task('styles', styles);
gulp.task('styles:django', stylesDjango);
gulp.task('styles:watch', stylesWatch);

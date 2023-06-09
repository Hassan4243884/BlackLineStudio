import gulp from 'gulp';
import svgmin from 'gulp-svgmin';
import svgStore from 'gulp-svgstore';
import rename from 'gulp-rename';
import cheerio from 'gulp-cheerio';
import through2 from 'through2';
import consolidate from 'gulp-consolidate';
import config from '../../config';

export const svgSprite = () => (
    gulp.src(config.src.icons + '/**/*.svg').
        pipe(svgmin({
          js2svg: {
            pretty: true,
          },
          plugins: [
            {
              removeDesc: true,
            }, {
              cleanupIDs: true,
            }, {
              mergePaths: false,
            }],
        })).
        pipe(rename({prefix: 'svg-ico_'})).
        pipe(svgStore({inlineSvg: false})).
        pipe(cheerio({
          run: function($, file) {
            $('[fill]:not([fill="currentColor"])').removeAttr('fill');
            $('[stroke]').removeAttr('stroke');
          },
          parserOptions: {xmlMode: true},
        })).
        pipe(through2.obj(function(file, encoding, cb) {
          const $ = file.cheerio;
          const data = $('svg > symbol').map(function() {
            const $this = $(this);
            const size = $this.attr('viewBox').split(' ').splice(2);
            const name = $this.attr('id');
            const ratio = size[0] / size[1];
            const fill = $this.find('[fill]:not([fill="currentColor"])').attr('fill');
            const stroke = $this.find('[stroke]').attr('stroke');
            return {
              name: name,
              ratio: +ratio.toFixed(2),
              fill: fill || 'initial',
              stroke: stroke || 'initial',
            };
          }).get();
          this.push(file);
          gulp.src(__dirname + '/_svg-ico.scss').pipe(consolidate('lodash', {
            symbols: data,
          })).pipe(gulp.dest(config.src.scssGenerated));
          // gulp.src(__dirname + '/sprite.html')
          // .pipe(consolidate('lodash', {
          //   symbols: data
          // }))
          // .pipe(gulp.dest(config.src.includes));
          cb();
        })).
        pipe(rename({basename: 'sprite'})).
        pipe(gulp.dest(config.src.img))
);

export const svgSpriteWatch = () => (
    gulp.watch(config.src.icons + '/**/*.svg', svgSprite)
);

gulp.task('svg:sprite', svgSprite);
gulp.task('svg:sprite:watch', svgSpriteWatch);
import path from 'path';

const webpackConfig = {
  mode: 'production',
  output: {
    path: path.resolve(__dirname, '../src'),
    filename: '[name].js',
    chunkFilename: '[name].js',
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        vendors: {
          test: /([\\/]node_modules[\\/]|[\\/]app_vendors[\\/])/,
          name: 'vendor',
          chunks: 'all',
          minSize: 30
        }
      }
    },
  },
  module: {
    rules: [
      {
        use: 'babel-loader',
        test: /\.(js)$/,
        exclude: /node_modules/,
      },
    ],
  },
};

export default webpackConfig;
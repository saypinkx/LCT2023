const { isDev } = require('./webpack/webpack.helpers');

module.exports = {
  presets: ['@babel/preset-env', '@babel/preset-react'],
  plugins: isDev() ? ['react-refresh/babel'] : [],
};

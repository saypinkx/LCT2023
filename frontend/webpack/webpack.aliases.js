const { createWebpackAliases } = require('./webpack.helpers');

/**
 * Some text editors will show the errors or invalid intellisense reports
 * based on these webpack aliases, make sure to update `tsconfig.json` file
 * also to match the `paths` we're using in here for aliases in project.
 */
module.exports = createWebpackAliases({
  '@assets': 'assets',
  '@src': 'src',
});

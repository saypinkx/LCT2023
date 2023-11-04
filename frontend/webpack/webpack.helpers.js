const cwd = process.cwd();
const path = require('path');

function createWebpackAliases(aliases) {
  const result = {};
  for (const name in aliases) {
    result[name] = path.join(cwd, aliases[name]);
  }
  return result;
}

function isDev() {
  return process.env.NODE_ENV === 'development';
}

module.exports = { createWebpackAliases, isDev };

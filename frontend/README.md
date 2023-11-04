## Core Features

- ⚛️ React
- 🌀 TypeScript
- 🛶 LESS Loader
- 🎨 CSS Loader
- 📸 Image Loader
- 🆎 Font Loader
- 🧹 ESLint
- 🔱 Webpack & Configuration
- 🧩 Aliases for project paths
- 🔥 Hot Module Replacement (Live Reload)

## Start : Development

To develop and run your web application, you need to run following command :

```bash
npm start
```

<br />

## Lint : Development

To lint application source code using ESLint via this command :

```bash
npm lint
```

<br />

## Build : Production

Distribution files output will be generated in `dist/` directory by default.

To build the production ready files for distribution, use the following command :

```bash
npm build --legacy-peer-deps
```

<br />

## Webpack Configurations

To make it easier for managing environment based webpack configurations, we using separated `development` and `production` configuration files, they are available in :

```bash
tools/webpack/webpack.config.dev.js
tools/webpack/webpack.config.prod.js
```

For further information, you can visit [Webpack Configuration](https://webpack.js.org/configuration/)

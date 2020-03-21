const path = require('path')

// vue.config.js
module.exports = {
  publicPath: './',
  configureWebpack: {
    resolve: {
      alias: {
        _assets_: path.resolve(__dirname, '/src/assets')
      }
    }
  }
}
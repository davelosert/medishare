const path = require('path')

const envPath = process.env.NODE_ENV === 'production' ? 'main' : 'dev'

// vue.config.js
module.exports = {
  publicPath: './',
  configureWebpack: {
    resolve: {
      alias: {
        api: path.resolve(__dirname, `src/api/${envPath}`)
      }
    }
  }
}
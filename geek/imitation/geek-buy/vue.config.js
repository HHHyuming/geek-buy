const path = require('path');

module.exports = {
    lintOnSave:false,
    configureWebpack:{
        resolve:{
            alias:{
                '@': path.resolve('./src'),
                'images': path.resolve('./src/images')
            }
        },

    }
}

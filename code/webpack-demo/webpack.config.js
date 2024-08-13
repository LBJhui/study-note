const path = require('path');

module.exports = {
  mode: 'development', // 'development' | 'production'
  // entry: './src/index.js',
  entry: {
    main: './src/index.js',
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};

var debug = require('debug')('mydebug:work');
setInterval(function () {
  debug('doing some work @ %s —— %s', new Date().getTime(), 'with supervisor');
}, 2000);

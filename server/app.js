var express = require('express'),
request=require("request");
var app  = module.exports = express();

var options = {
    host : 'http://127.0.0.1',
    port : 6699,
    path: '/',
    method : 'POST'
};

app.configure(function() {
  app.set('views', __dirname + '/server/views');
  app.set('view engine', 'jade');
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(stylus.middleware(
    {
      src: __dirname + '/public',
      compile: compile
    }
  ));
  app.use(express.static(__dirname + '/public'));
});


app.get('/partials/:partialPath', function(req, res) {
  res.render('partials/' + req.params.partialPath);
});

app.get('*', function(req, res) {
  res.render('index');
});

request.get(options,function(error,response,body){
    if(error){
        console.log(error);
    }else{
        console.log(response);
    }
});


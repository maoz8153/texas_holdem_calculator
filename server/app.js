var express = require('express'),
    request=require("request");

var env = process.env.NODE_ENV = process.env.NODE_ENV || 'development';

var app = express();


var options = {
    host : 'http://127.0.0.1',
    port : 6699,
    path: '/',
    method : 'POST'
};







/*request.get(options,function(error,response,body){
    if(error){
        console.log(error);
    }else{
        console.log(response);
    }
});*/

app.use(express.static(__dirname + '/views'));
app.set('views',__dirname + '/views');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);


app.get('/',function(req,res){

          res.render('index');

});


var server=app.listen(3000,function(){
console.log("Express is running on port 3000");
});

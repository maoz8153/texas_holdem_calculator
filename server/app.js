var express = require('express'),
request=require("request");
var app  = module.exports = express();

var options = {
    host : 'http://127.0.0.1',
    port : 6699,
    path: '/',
    method : 'POST'
};

request.get(options,function(error,response,body){
    if(error){
        console.log(error);
    }else{
        console.log(response);
    }
});


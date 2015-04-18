var express = require('express'),
request=require("request");
var app  = module.exports = express();

var options = {
    url: 'http://127.0.0.1:9988'
};

request.get(options,function(error,response,body){
    if(error){
        console.log(error);
    }else{
        console.log(response);
    }
});


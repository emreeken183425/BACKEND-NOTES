
const http=require('http');
const fs=require('fs');
// server üzerinden eventemitter aldık 
const server=http.createServer((req,res)=>{
   
    // // response header kısmı
    // // res.setHeader('contet-type','text/plain')
    // // **JSON TİPİ VERİ GÖNDERME***//
    // // res.setHeader('contet-type','application/json')
    // // res.write(JSON.stringify({name:'redmi 9 pro',price:3000}));
    // // HTML TİPİ VERİ GÖNDERME
    // res.setHeader('Content-Type','text/html');
    // res.statusCode=200;
    // res.statusMessage="OK";

    // //response body kısmı
    // res.write('<html>');
    // res.write('<head><title>My first page</title></head>');
    // res.write('<body><h1>Hello from Nodejs Server</h1></body>')
    // res.write('</html>')
    // res.end();
   fs.readFile('index.html',function(error,file){
    if(error){
        res.setHeader('Content-Type','text/plain');
        res.statusCode=404;
        res.statusMessage='not found'
      // bunu yazabilirsin yada yerine   res.write('dosya bulunamadı')
        res.end('dosya bulunamadı')// bunu şekilde yazılır
    }else{
        res.setHeader('Content-Type','text/html');
        res.statusCode=200;
        res.statusMessage='ok'
        res.end(file)
    }
   })


} );


server.listen(3000);
 
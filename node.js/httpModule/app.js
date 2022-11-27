const http=require('http');

const server=http.createServer((req,res)=>{
   if(req.url==='/'){
    res.write('hello world');
    res.end();
   }
   if(req.url==='/api/products'){
    res.write('product list')
    res.end();
   }
});

server.on('connection',function(){
    console.log('new connection...');
})
server.listen(3000);
 console.log('listening port 3000 ...');
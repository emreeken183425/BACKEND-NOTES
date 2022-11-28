const express=require('express');

const app=express();

// app.get('/',(req,res)=>{
//     res.send('hello world')
// });

// app.get('/api/products',(req,res)=>{
//     res.send('ürünler listelendi')
// })

app.use((req,res,next)=>{
    console.log("middleware 1 çalıştırıldı");
    res.send('<h1>hello from express.js</h1> ')
})
app.listen(3000,()=>{
    console.log('listening on port 3000');
})


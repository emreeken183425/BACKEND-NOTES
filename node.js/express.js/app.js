const express=require('express');

const app=express();
const bodyParser=require('body-parser')
const adminRoutes=require('./routes/admin')  
const userRoutes=require('./routes/user')



app.use(bodyParser.urlencoded({extended:false}))  
app.use(adminRoutes)
app.use(userRoutes)

app.set('title','My site');
console.log(app.get('title'));


app.use('/add-list',(req,res,next)=>{
       
            res.send('<h1>adding list page</h1> ')
            })

           
 // yukarıdakini yazınca aşağıdakine geçmiyor bu sebeple sıralama önemli   bunu engellemek için ilk dizine next() konulur   



        /* 
    <!-- middleware işlemi yapıyoruz -->
app.use((req,res,next)=>{
console.log("middleware 1 çalıştırıldı");
next();
})
app.use((req,res,next)=>{
    console.log("middleware 2 çalıştırıldı");
    res.send('<h1>hello from express.js</h1> ')
})
*/
    

 /* get işlemi yaptık
 app.get('/',(req,res)=>{
     res.send('hello world')
 });

 app.get('/api/products',(req,res)=>{
     res.send('ürünler listelendi')
 })
 */


// burada hangi port üzerinde çalışacağımızı yazdık
app.listen(3000,()=>{
    console.log('listening on port 3000');
})


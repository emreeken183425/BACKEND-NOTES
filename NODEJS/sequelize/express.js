const express=require('express')
const app =express();
const db=require('./database')
const opRoute=require('./routes/op-route')



app.use(express.json())// req.body .alışması için 




db.CONNECT_DB();


app.use(opRoute)




const port=5000;
app.listen(port,()=>{
    db.REFRESH_DB();// bir kere çalıştır databsede oluştu sonra yoruma al almassan tekrar aynısı oluşur
    console.log(`localhost:${port} is active `);
})
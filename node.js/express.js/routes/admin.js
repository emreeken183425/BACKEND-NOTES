
const express =require('express')
const router=express.Router()



router.get('/add-product',(req,res,next)=>{
       
    res.send(`
    <html >
<head>

<title>add new product</title>
</head>
<body>
<form action="/add-product" method="POST"  >
    <input type="text" name="productName" >
    <input type="submit" value="saveProduct" >
</form>
</body>
</html>
    `)
    })
// use mehodu ile hem get hem post yapıyoruz sadece post iiçin use yerine post yazmak yeterli
router.post("/product",(req,res,next)=>{
console.log(req.body);
//istediğimiz yere yönlendirme
res.redirect("/")
})

module.exports=router
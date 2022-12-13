nodejs kurulum 
npm init -y

 paketleri indirdik
npm i express sequelize pg pg-hstore nodemon

package.json e gidip 

"start": "nodemon express.js", yazıyoruz 


Middleware işlemleri
AdminMiddleware file
"""
const checkAdmin=(req,res,next)=>{
const user=req.body;
if(user.role !='admin'){
    return res.status(403).json({message:"Forbidden Error"})
}
next();
}

module.exports={
    checkAdmin
}
"""
express.js 
"""
const aMiddleware=require('./adminMiddleware')

app.use(express.json());

app.use((req,res,next)=>{
    console.log('Global Middleware works');
    next();
})

app.post('/',aMiddleware.checkAdmin,(req,res)=>{
    return res.json(req.body)
})
"""

 // ***  HTTP METHOTLARI  ****



//***    GET İŞLEMİ    ***/
app.get('/users',(req,res)=>{
    // db ye erişilip esponse return edilmeli
    return res.status(200).json(users)
})

//***    POST İŞLEMİ    ***/
app.post('/create',(req,res)=>{
  const {fullname,age,role}=req.body // gelen req ten aldık
  //""" app.use(express.json())"""" req.body çalışması için post    işleminde middlewara yazmak lazım 
  const newUser={
    fullname,
    age,
    role
  }; // req den aldıklarımızı new userda nerelere gelmesi gerekiyor atadık
  users.push(newUser);// newUser a kaydettik
  return res.status(201).json(users)// newUser döndürdük
})

//***    DELETE İŞLEMİ    ***/

app.delete('/:id',(req,res)=>{
    const id=req.params.id;// id tanımladık silmek istediğimiz bölüm için
    users=users.filter((user)=>user.id !==id)// filter ile id ye eriştik
    return res.json(users)// ve kalan  kullanıcıları döndürdük 
})

//***    PUT/UPDATE İŞLEMİ    ***/

app.put('/user/:id',(req,res)=>{
    const id=req.params.id;// id ile users içinden çağırdık
    const {fullname}=req.body;// değiştirecek alanı seçtik 
    users.forEach((user)=>{ // forEach ile ilgili bölüme ulaşıp değiştireceğimiz alanı yazdık
        if(user.id===id){
user.fullname=fullname;
        }
    })
    return res.json(users)// ve yeni  kullanıcıları döndürdük 
})






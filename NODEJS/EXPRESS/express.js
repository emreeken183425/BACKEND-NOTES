const express=require('express')
const app =express();


app.use(express.json())// req.body çalışması için post işleminde middlewara yazmak lazım 

var users=[
    {id:"1" , fullname:"ahmet özdemir",age:23,role:"admin"},
    {id:"2"  ,fullname:"emre eken",age:30,role:"admin"},
    {id:"3"  ,fullname:"yasemin eken",age:27,role:"user"}
]




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


const port=4000;
app.listen(port,()=>{
    console.log(`localhost:${port} is active `);
})
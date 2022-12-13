const userModel = require("../models/user-models");


//**** POST İŞLEMİ  ****/
const  createOne=async(req,res)=>{
    try {
        const {username,password}=req.body;
        const newUser=await userModel.create({
            username,
            password
        })
       return res.status(201).json(newUser)

    } catch (err) {
        return res.json({message:err.message})
    }
}



//**** BİRDEN FAZLA POST İŞLEMİ  ****/
const  bulkCreate=async(req,res)=>{
    try {
        const newUsers=await userModel.bulkCreate(req.body);
        return res.status(201).json(newUsers)


    } catch (err) {
        return res.json({message:err.message})
    }
}

//**** GET İŞLEMİ  ****/
const  find=async(req,res)=>{
    try {
        const user=await userModel.findAll();
        return res.json(user)


    } catch (err) {
        return res.json({message:err.message})
    }
}

//**** PUT/UPDATE İŞLEMİ  ****/
const  update=async(req,res)=>{
    try {
        const {username}=req.body;
       const changeUser= await userModel.update({username:username},{
            where:{
                username:"emre2"
            }
        })
return res.json(changeUser)
    } catch (err) {
        return res.json({message:err.message})
    }
}

//**** DELETE İŞLEMİ  ****/
const  delItem=async(req,res)=>{
    try {
        const id=req.params.id;
        await userModel.destroy({where:{
            id:id
        }})
        return res.json();
    } catch (err) {
        return res.json({message:err.message})
    }
}





module.exports={
createOne,
bulkCreate,
find,
update,
delItem
}
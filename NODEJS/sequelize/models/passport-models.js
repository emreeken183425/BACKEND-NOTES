// ilk önce databse import ediyoruz const db=require('../database')
const { DataTypes } = require('sequelize')
const db=require('../database')


// sonra tablomuzu oluşturuyoruz
// User burada modelin adı sonrası kolonları 
const passportModel=db.sequelize.define('Passport',{
    country:{
        type:DataTypes.STRING(50),
        allowNull:false,
        unique:true,
    }
},
{
    createAt:true,
    deleteAt:true,
    version:true,
    updateAt:true,

})

module.exports=passportModel;
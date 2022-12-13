// ilk önce databse import ediyoruz const db=require('../database')
const { DataTypes } = require('sequelize')
const db=require('../database')


// sonra tablomuzu oluşturuyoruz
// User burada modelin adı sonrası kolonları 
const movieModel=db.sequelize.define('Movie',{
    username:{
        type:DataTypes.STRING(50),
        allowNull:false,
        
    },
    
},
{
    createAt:true,
    deleteAt:true,
    version:true,
    updateAt:true,

})

module.exports=movieModel;
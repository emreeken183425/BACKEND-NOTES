// ilk önce databse import ediyoruz const db=require('../database')
const { DataTypes } = require('sequelize')
const db=require('../database')


const flightModel=db.sequelize.define('Flight',{
    to:{
        type:DataTypes.STRING(50),
        allowNull:false,
     
    },
    from:{
        type:DataTypes.STRING(50),
        allowNull:false,
     
    }
    
},
{
    createAt:true,
    deleteAt:true,
    version:true,
    updateAt:true,

})

module.exports=flightModel;
const Sequelize=require('sequelize')

const sequelize=new Sequelize('node-app','root','Erzurum25!',{
  dialect:'mysql',
  host:'localhost'
})

module.exports=sequelize;
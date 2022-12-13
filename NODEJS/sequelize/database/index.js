// sequelize import ettik ilk önce
const Sequelize = require("sequelize");
let db = {};
// postgresql ile bağlantı kurduk burada
const sequelize = new Sequelize({
  host: "localhost",
  dialect: "postgres",
  database: "express",
  username: "postgres",
  password: "183425",
  port: 5433,
  pool: 40,
  retry: 3,
  logging: true,
});

const CONNECT_DB = async (req, res) => {
  try {
    await sequelize.authenticate({ logging: true });
    console.log("sequelzie bağlandı");
  } catch (error) {
    return console.log(`${error.message} `);
  }
};

const REFRESH_DB = async () => {
  try {
    const userModel = require("../models/user-models");
    const passportModel = require("../models/passport-models");
    const flightModel = require("../models/fligtTicket-Models");
    const movieModel=require("../models/movie-models")
    const usermovieModel=require("../models/user-movie-models")


    // one to one ilişki
    userModel.hasOne(passportModel, {
      foreignKey: "user_id",
    });
    passportModel.belongsTo(userModel);

    // one to -many ilişki
    userModel.hasMany(flightModel, {
      foreignKey: "user_id",
    });
    flightModel.belongsTo(userModel);


    //many to many ilişki 
    userModel.belongsToMany(movieModel,{through:usermovieModel})
    movieModel.belongsTo(userModel,{through:usermovieModel})




    
    // userModel.sync({ force: true });
    // passportModel.sync({ force: true });
    // flightModel.sync({ force: true });
    // movieModel.sync({force:true});
sequelize.sync({force:true})

  } catch (error) {
    return console.log(`${error.message} `);
  }
};

db.CONNECT_DB = CONNECT_DB;
db.sequelize = sequelize;
db.REFRESH_DB = REFRESH_DB;
// export ettik en son sonra expressjs e gidip çağıracağız
//expressjs te aşağıdaki gibi çağıracağız
// const db=require('./database') ile import
//db.CONNECT_DB(); ile çağırdık

module.exports = db;

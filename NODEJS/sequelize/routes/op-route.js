const express=require('express')
const router=express.Router();
const opCtrl=require('../controllers/op-ctrl')




router.route('/create').post(opCtrl.createOne);
router.route('/bulkcreate').post(opCtrl.bulkCreate);

router.route('/find').get(opCtrl.find);


router.route('/update').put(opCtrl.update);


router.route('/delete/:id').delete(opCtrl.delItem);



module.exports=router
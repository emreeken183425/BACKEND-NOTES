
//https://nodejs.org/dist/latest-v18.x/docs/api/events.html

const EventEmitter=require('events');
const emitter=new EventEmitter();
// logger dosyamızı import ettik 
const Logger=require('./logger')
const logger=new Logger();
// listener kayıt et(args ilebirden fazla parametre göndeririz)

logger.on('connection',function(args){
    console.log('bağlantı kuruldu',args);
})


//eventi tetikle ({id:1,message:'hello'} args içine gönderidğimiz parametreler)
emitter.emit('connection',{id:1,message:'hello'} )

logger.log('emre giriş yaptı')



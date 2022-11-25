var controllerA=(function(){
    var firstName="eken";
    var log=function(){
        console.log(this.firstName);
    }
    return{
        firstName,
        log
    }
}

)
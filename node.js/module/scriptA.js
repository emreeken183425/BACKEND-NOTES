 //scrtiptA bir module 
 
// firstname modulumüz içinde tanıdığımız değişken 
var firstName="emre";

// fonsksiyon tanımlama aşağıdaki şekilde
var log=function(name){
    console.log(name);
}

console.log(__filename);

// tanıdğımız fonsiyon ve değşkenş dışarı açmak istiyorsak yani
//dışarıdan bu yazdığımız fonsiyon yada değişken ulaşılmasını istiyorsak 
//module.export(dışarı aktarırken başta)name(istediğini yaz)=firsName(değişken yada fonsiyon ismi yazılır)

// module.export.name=firstName;
// module.export.log=log;


 //tek tek yukarıdaki gibi yazmak yerine aşağıdaki gibi yapıla bilir 
 module.export={
    name: firstName,
      log:log
 }

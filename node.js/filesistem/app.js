
//https://nodejs.org/dist/latest-v18.x/docs/api/fs.html

// herhangi bir dosya içerisine ulaşıp istediğimiz işlemi yapabiliriz
const fs=require('fs');

// klasör okumak burada uyguklama devam ederken bir yandan istediğimiz gelir sekron türü
// dosya bulduk burada
const files=fs.readdir('./',function(error,data){

if(error){
    console.log(error);
}else{
    console.log(data);
}


})

// örneğin index html dosyasını yazdıralım 

const data1=fs.readFile('index.html','utf8',function(err,data1){
    if(err){
        console.log(err);
    }else{
        console.log(data1);
    }
})

// DOSYA OLUŞTURMA (writeFile önceki içeriği değiştirir hello world yerie bir şey yazarsak )'Hello World ...'
// appendFile ise önceki içerik üzerinde yazar yani önceki içerik + eklenenle birlikte önceki içerik 'Hello World'+'Hello World ...'
fs.writeFile('deneme.txt','Hello World',function(err){
    if(err){
        console.log(err);
    }else{
        console.log('dosya oluşturuldu');
    }
} )

// fs.appendFile('deneme1.txt','hello world',function(err){
//     if(err){
//         console.log(err);
//     }else{
//         console.log('appen file ile oluştu');
//     }
// })

//  dosya silme işlemleri


fs.unlink('deneme.txt',function(err){
    console.log('dosaya silindi');
} )

// dosya ismi değişme 

fs.rename('deneme1.txt','deneme3.txt',function(err){
    console.log('isim değişti');
})
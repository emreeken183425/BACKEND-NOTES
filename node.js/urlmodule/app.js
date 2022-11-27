//https://nodejs.org/dist/latest-v18.x/docs/api/url.html

// uygulamaya gelen adres içerisindeki bölümlere ulaşmak için 
const url=require('url');

const address='http://sadikturan.com/kurslar?year=2019&month=nisan';
 let result=url.parse(address,true);
 console.log(result);
 console.log(result.path);
const path=require('path');
//https://nodejs.org/dist/latest-v18.x/docs/api/path.html
// path içinde bulunduğu yeri yazdırırız bu şekilde
let result=path.resolve('app.js');

result=path.extname("app.js")
result=path.parse(__filename)
console.log(result);
const http = require("http");
const fs = require("fs");
const server = http.createServer((req, res) => {
  const url = req.url;
  const method = req.method;
  res.setHeader("Content-Type", "text/html");
  if (url === "/") {
    res.write(`
        <html>
        <head>
        <title>
       routing method
        </title>
        </head>
        <body>
        <form method="POST" action="/log"  >
        <input type="text" name="message"   />
        <button type="submit" action="/message" >Save</button>
        </form>
        </body>
        </html>
        `);
    return res.end();
  }
  if (url === "/log" && method === "POST") {



    
    fs.appendFileSync("message.txt", "deneme");
    res.statusCode = 302;
    res.setHeader("Location", "/");
    return res.end();
  }
});
server.listen(3000);

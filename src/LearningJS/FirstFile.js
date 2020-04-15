const path = require("path");


var hello = "Hello World From NODE JS";

console.log(`The file name is ${path.basename(__filename)}`);



console.log(hello);
console.log(__dirname);
console.log(__filename);
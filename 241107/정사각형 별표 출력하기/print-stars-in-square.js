let str = "";
const fs = require("fs");
let input = Number(fs.readFileSync(0).toString().trim());


for (let i = 0; i < input; i++) {
    str = "";
    for (let j = 0; j < input; j++) {
        str += "*";
    }
    console.log(str);
}
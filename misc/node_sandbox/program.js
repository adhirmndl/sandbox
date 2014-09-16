var fs = require('fs');
buff = fs.readFileSync(process.argv[2]);
contents = buff.toString();
console.log(contents.split('\n').length - 1)
// nLines = 0;
// for (i = 0; i < contents.length; i++){
// 	if (contents[i] == '\n'){
// 		nLines += 1;
// 	}
// }

// console.log(nLines)
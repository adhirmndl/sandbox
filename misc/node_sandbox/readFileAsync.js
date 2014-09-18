var fs = require('fs');
function wordcount(err, buff){
	contents = buff.toString();
	console.log(contents.split('\n').length - 1)
}
buff = fs.readFile(process.argv[2], wordcount);

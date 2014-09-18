var fs = require('fs');
var path = require('path');

function filterls(err, listoffiles){
	for(i = 0; i < listoffiles.length; i++){
		if (path.extname(listoffiles[i]).indexOf(process.argv[3]) != -1) {
			console.log(listoffiles[i]);
		}
	}
}
fs.readdir(process.argv[2], filterls);

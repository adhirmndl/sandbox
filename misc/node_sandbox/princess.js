var fs = require('fs')
 , sys = require('sys');

fs.readFile('report.txt', function(report){
	sys.puts("The money! " + report);
});
fs.writeFile('letter.txt', 'muah, more muah', function(){
	sys.puts("stuff has been written");
});

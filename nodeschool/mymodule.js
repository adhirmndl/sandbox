// mymodule.js

var fs = require('fs')
var path = require('path')

// FILETERED LS
// ============
function filteredls(arg, extname, callback){
	fs.readdir(arg, function(err, list){
		if (err)
			return callback(err)
		var data = []
		list.forEach( function (file) {
			if (path.extname(file) === '.' + extname)
				data.push(file)
		})
		return callback(null, data)
	})
}

module.exports = filteredls

// module.exports = function (dir, filterStr, callback) {
//   	fs.readdir(dir, function (err, list) {
//     if (err)
//       return callback(err)

//     list = list.filter(function (file) {
//       return path.extname(file) === '.' + filterStr
//     })

//     callback(null, list)
//   })
// }

// console.log('ALL YOUR ' + process.argv[2] + ' ARE BELONG TO ' + process.argv[3])

// GET YOUR LEVEL ON
// =================

// var level = require('level')
// var db = level(process.argv[2])

// db.get(process.argv[3], function (err, value){
// 	if (err)
// 		throw err
// 	console.log(value)
// })

// GET
// ===
var level = require('level')
var db = level(process.argv[2])

var getNext = function (i) {
	var key = 'key' + i
	db.get(key, function (err, value){
		if (err) {
			if (!err.notFound)
				throw (err)
		} else
			console.log(key + '=' + value)
		if (i < 100)
			getNext(i+1)
	})
}
getNext(0)
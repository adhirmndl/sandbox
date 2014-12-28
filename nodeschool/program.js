// HELLO WORLD
// ===========
// console.log("HELLO WORLD")

// BABY STEPS
// ==========
// var args = process.argv
// var sum = 0
// for (var i = 2; i < args.length; i++) {
// 	sum = sum + Number(args[i])
// }
// console.log(sum)

// MY FIRST I/O
// ============
// var fs = require('fs')
// var contents = fs.readFileSync(process.argv[2]).toString().split('\n')
// console.log(contents.length - 1)

// MY FIRST ASYNC I/O
// ==================
// var fs = require('fs')
// var lc = function (err, contents){
// 	console.log(contents.toString().split('\n').length - 1)
// }
// var contents = fs.readFile(process.argv[2], lc)

// FILTERED LS
// ============
// var fs = require('fs')
// var path = require('path')
// fs.readdir(process.argv[2], function (err, list) {
//   list.forEach(function (file) {
//     if (path.extname(file) === '.' + process.argv[3])
//       console.log(file)
//   })
// })

// MAKE IT MODULAR
// ===============
// var mymodule = require('./mymodule.js')
// mymodule(process.argv[2], process.argv[3], function(err, data){
// 	if (err)
// 		return console.log('error occurred!', err)
// 	data.forEach(function(file){
// 		console.log(file)
// 	})
// })

// HTTP CLIENT
// ===========
// var http = require('http')
// var req = http.get(process.argv[2], function(response){
// 	response.setEncoding('utf8')
// 	response.on("data", console.log)
// 	response.on("error", console.error)
// })

// HTTP COLLECT
// ============
var http = require('http')
var bl = require('bl')
// var mybl = bl(function(err, data){
// 	console.log(data)
// })
var masterData = ""
var req = http.get(process.argv[2], function(response){
	response.setEncoding('utf8')
	response.on('data', function(data){
		masterData.append(data.toString())
	})
	response.on('end', function(data){
		console.log(masterData)
	})
})

// HTTP 
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
// var http = require('http')
// var masterData = ""
// var req = http.get(process.argv[2], function(response){
// 	response.setEncoding('utf8')
// 	response.on('data', function(data){
// 		masterData = masterData + data
// 	})
// 	response.on('end', function(data){
// 		console.log(masterData.length)
// 		console.log(masterData)
// 	})
// })

// HTTP COLLECT (OFFICIAL)
// =======================
// var http = require('http')
// var bl = require('bl')

// http.get(process.argv[2], function (response) {
//   response.pipe(bl(function (err, data) {
//     if (err)
//       return console.error(err)
//     data = data.toString()
//     console.log(data.length)
//     console.log(data)
//   }))  
// })


// JUGGLING ASYNC 
// ==============

// var http = require('http')
// var bl = require('bl')
// var dataArr = [] 
// var flag = [] 
// for (var i = 0; i < 3; i++) {
// 	flag[i] = false
// 	dataArr[i] = ""
// }
// var getURLContents = function(url, i){
// 	http.get(url, function(response){
// 		response.pipe(bl(function(err, data){
// 			if (err)	
// 				return console.error(err)
// 			// console.log("data received from: " + url)
// 			dataArr[i] = data.toString()
// 			flag[i] = true
// 			printContents()
// 		}))	
// 	})	
// }

// var printContents = function(){
// 	for (var i = 0; i < flag.length; i++) {
// 		if(!flag[i])
// 			return false
// 	}
// 	for (var i = 0; i < dataArr.length; i++) {
// 		console.log(dataArr[i])
// 	};
// }
// for (var i = 0; i < 3; i++) {
// 	getURLContents(process.argv[i+2], i)
// }

// JUGGLING ASYNC (OFFICIAL)
// =========================

// var http = require('http')
// var bl = require('bl')
// var results = []
// var count = 0

// function printResults () {
//   for (var i = 0; i < 3; i++)
//     console.log(results[i])
// }

// function httpGet (index) {
//   http.get(process.argv[2 + index], function (response) {
//     response.pipe(bl(function (err, data) {
//       if (err)
//         return console.error(err)

//       results[index] = data.toString()
//       count++

//       if (count == 3) // yay! we are the last one!
//         printResults()
//     }))
//   })
// }

// for (var i = 0; i < 3; i++)
//   httpGet(i)

// TIME SERVER
// ===========

// var net = require('net')
// var strftime = require('strftime')
// var server = net.createServer(function(socket){
// 	var data = strftime('%F %H:%M\n')
// 	socket.write(data)
// 	socket.end()
// })
// server.listen(Number(process.argv[2]))

// TIME SERVER (OFFICIAL)
// ======================

// var net = require('net')
// function zeroFill(i) {
//   return (i < 10 ? '0' : '') + i
// }

// function now () {
//   var d = new Date()
//   return d.getFullYear() + '-'
//     + zeroFill(d.getMonth() + 1) + '-'
//     + zeroFill(d.getDate()) + ' '
//     + zeroFill(d.getHours()) + ':'
//     + zeroFill(d.getMinutes())
// }

// var server = net.createServer(function (socket) {
//   socket.end(now() + '\n')
// })

// server.listen(Number(process.argv[2]))

// HTTP FILE SERVER
// ================
// var http = require('http')
// var fs = require('fs')
// var server = http.createServer(function(request, response){
// 	response.writeHead(200, { 'content-type' : 'text/plain' })
// 	fs.createReadStream(process.argv[3]).pipe(response)
// })
// server.listen(Number(process.argv[2]))

// HTTP UPPERCASERER
// =================

// var http = require('http')
// var map = require('through2-map')

// var server = http.createServer(function(req, res){
// 	if (req.method.toString() == 'POST'){
// 		req.pipe(map(function(chunk){
// 			return chunk.toString().toUpperCase()
// 		})).pipe(res)
// 	} else {
// 		return res.end("send a POST\n")
// 	}
// })
// server.listen(process.argv[2])

// HTTP JSON API SERVER
// ====================

var http = require('http')
var url = require('url')
var server = http.createServer(function(req, res){
	if ( req.method == 'GET'){
		var reqURL = url.parse(req.url, true)
		res.writeHead(200, { 'Content-type' : 'application/json'})

		if (reqURL.pathname == ('/api/parsetime')){
			var d = new Date(reqURL.query['iso'])
			res.write(JSON.stringify({
				hour: d.getHours(), 
				minute : d.getMinutes(), 
				second : d.getSeconds()
			}))
		}
		if (reqURL.pathname == ('/api/unixtime')){
			var d = new Date(reqURL.query['iso'])
			res.write(JSON.stringify({
				unixtime : d.getTime()
			}))
		}
	} else{
		res.write("Send me a GET on /api/parsetime\n")
	}
	res.end()
})
server.listen(process.argv[2])

// HTTP JSON API SERVER (OFFICIAL)
// ===============================

// var http = require('http')
// var url = require('url')

// function parsetime (time) {
//   return {
//     hour: time.getHours(),
//     minute: time.getMinutes(),
//     second: time.getSeconds()
//   }
// }

// function unixtime (time) {
//   return { unixtime : time.getTime() }
// }

// var server = http.createServer(function (req, res) {
//   var parsedUrl = url.parse(req.url, true)
//   var time = new Date(parsedUrl.query.iso)
//   var result

//   if (/^\/api\/parsetime/.test(req.url))
//     result = parsetime(time)
//   else if (/^\/api\/unixtime/.test(req.url))
//     result = unixtime(time)

//   if (result) {
//     res.writeHead(200, { 'Content-Type': 'application/json' })
//     res.end(JSON.stringify(result))
//   } else {
//     res.writeHead(404)
//     res.end()
//   }
// })
// server.listen(Number(process.argv[2]))
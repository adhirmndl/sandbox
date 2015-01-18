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

// var level = require('level')
// var db = level(process.argv[2])

// var getNext = function (i) {
// 	var key = 'key' + i
// 	db.get(key, function (err, value){
// 		if (err) {
// 			if (!err.notFound)
// 				throw (err)
// 		} else
// 			console.log(key + '=' + value)
// 		if (i < 100)
// 			getNext(i+1)
// 	})
// }
// getNext(0)

// PUT
// ===

// var level = require('level')
// var db = level(process.argv[2])
// var jsonObj = JSON.parse(process.argv[3])

// for (var key in jsonObj) {
// 	db.put(key, jsonObj[key], function(err){
// 		if (err)
// 			return console.error('Error in put(): ', err)
// 	})
// }

// BATCH
// =====

// var level = require('level')
// var fs = require('fs')
// var db = level(process.argv[2])
// var batchDB = function(err, data){
// 	if (err)
// 		throw err
// 	var ops = data.toString().split('\n')
// 	var batchOps = []
// 	ops.forEach(function(op){
// 		opArray = op.split(',')
// 		var operation = {}
// 		operation['type'] = opArray[0]
// 		operation['key'] = opArray[1]
// 		if (opArray[0] == 'put')
// 			operation['value'] = opArray[2]
// 		batchOps.push(operation)
// 	})
// 	// console.log(batchOps)
// 	db.batch(batchOps)
// }
// var contents = fs.readFile(process.argv[3], batchDB)

// BATCH (OFFICIAL)
// ================

// var operations = data.map(function (line) {
// var d = line.split(',')
//   // 'value' is ignored for del
//   return { type: d[0], key: d[1], value: d[2] }
// })

// db.batch(operations, function (err) {
//   if (err)
//     throw err
//   db.close()
// })

// STREAM
// ======

// var level = require('level')
// var db = level(process.argv[2])

// db.createReadStream().on('data', function(data){
// 	console.log(data.key + '=' + data.value)
// })

// @hores_js Count
// ===============

// var tweetCount = function (db, date, callback){
// 	var count = 0
// 	db.createReadStream({start : date})
// 		.on('data', function(data){
// 			count++
// 		})
// 		.on('error', function(err){
// 			if(callback){
// 				callback(err)
// 				callback = null
// 			}
// 		})
// 		.on('end', function(){
// 			if(callback){
// 				callback(null, count)
// 				callback = null
// 			}
// 		})
// }

// module.exports = tweetCount

// @horse_js Tweets
// ================

// var tweetMessages = function (db, date, callback){
// 	var holder = []
// 	db.createReadStream({start: date, end: (date + '\xff')})
// 		.on('data', function(data){
// 			holder.push(data.value)
// 		})
// 		.on('error', function(err){
// 			if(callback){
// 				callback(err)
// 				callback = null
// 			}
// 		})
// 		.on('end', function(){
// 			if(callback){
// 				callback(null, holder)
// 				callback = null
// 			}
// 		})
// }

// module.exports = tweetMessages

// KEYWISE OFFICIAL
// ================

var level = require('level')
var db = level(process.argv[2], { valueEncoding: 'json' })
var data = require(process.argv[3])
var operations = data.map(function (row) {
  var key
  if (row.type == 'user')
    key = row.name
  else if (row.type == 'repo')
    key = row.user + '!' + row.name
  return { type: 'put', key: key, value: row }
})

db.batch(operations)
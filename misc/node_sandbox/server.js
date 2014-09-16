var http = require("http");
var url = require("url");

function start(route) {
	function onRequest(request, response){
		var pathname = url.parse(request.url).pathname;
		var uName = url.parse(request.url)["user"]
		console.log("Request Received for " + pathname + " by " + uName);
		route(pathname)
	  	response.writeHead(200, {"Content-Type": "text/plain"});
	  	response.write("Hello World");
	  	response.end();
	}
	http.createServer(onRequest).listen(8888);
	console.log("Server started");
}

exports.start = start;


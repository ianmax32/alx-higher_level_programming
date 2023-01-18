#!/usr/bin/node
// this script computes the number of completed
// tasks by user id

const req = require('request');
req.get(process.argv[2], (err, response, body) => {
	if(err){
		console.log(err);
	} else {
		const users = new Map();
		for(const user of JSON.parse(body)){
			const counters = [];
			if(user.completed){
				counters.push(user.userId);
			}
			users.set(user.userId, counters.length)
			
		}
		console.log(Object.assign({} ,users));
	}
});

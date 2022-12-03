#!/usr/bin/node

if(parseInt(process.argv[2]))
{
	let a = 0;
	while (a < process.argv[2])
	{
		console.log('X'.repeat(process.argv[2]));
		a++;
	}
}
else
{
	console.log('Missing size');
}

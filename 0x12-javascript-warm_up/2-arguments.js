#!/usr/bin/node
// this script prints a message according to the number of arguments passed

if (process.argv.length === 2)
{
	console.log('No argument');
}
else if (process.argv.length === 3)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}

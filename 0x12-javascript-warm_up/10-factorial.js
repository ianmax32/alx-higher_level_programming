#!/usr/bin/node

const a = process.argv[2];

function factorial(a)
{
	if (a === 0)
	{
		 return 1;
	}
	else if (process.argv.length === 2)
	{
		return 1;
	}
	else
	{
		return a * factorial(a - 1);
	}
}

console.log(factorial(a));

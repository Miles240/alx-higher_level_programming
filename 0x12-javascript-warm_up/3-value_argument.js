#!/usr/bin/node

const argsCount = process.argv.length - 2;

if (argsCount === 0) {
	console.log('No argument');
} else if (argsCount === 1) {
	console.log(process.argv[2]);
} else {
	for (let i = 2; i <= process.argv.length; i++) {
		console.log(process.argv[i]);
	}
}

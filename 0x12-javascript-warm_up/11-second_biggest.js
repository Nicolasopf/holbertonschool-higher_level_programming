#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);

} else {
  const args = (process.argv.splice(2, process.argv.length)).map((num) => parseInt(num));
  const max = Math.max(...args);
  const idx = args.indexOf(max);
  args.splice(idx, 1);
  console.log(Math.max(...args));
}

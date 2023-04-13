#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  let counter = 0;
  return function () {
    console.log(`${counter}: ${item}`);
    counter++;
  }
}

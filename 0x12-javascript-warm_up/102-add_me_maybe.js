#!/usr/bin/node
exports.addMayBe = function (number, theFunction) {
  number++;
  theFunction(number);
};

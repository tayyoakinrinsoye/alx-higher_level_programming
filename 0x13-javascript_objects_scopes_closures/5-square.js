#!/usr/bin/node
// class Square that inherits from Rectangle

Rectangle = require("./4-rectangle");

const Square = class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
}

module.exports = Square;
#!/usr/bin/node
//Class square that inherits from Square

const Square5 = require('./5-square');

class Square extends Square5 {
    charPrint(c) {
        if (c) {
            let pattern = '';
            for (let i = 0; i < this.height; i++) {
                for (let j = 0; j < this.height; j++) {
                    pattern = pattern + c;
                }
                console.log(pattern);
                pattern = '';
            }
        } else {
            super.print();
        }
    }
}
module.exports = Square;
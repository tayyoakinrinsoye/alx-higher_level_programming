#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let pattern = '';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        pattern = pattern + 'X';
      }
      console.log(pattern);
      pattern = '';
    }
  }
}
module.exports = Rectangle;

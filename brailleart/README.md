# Braille Art

#### todo

This is a work in progress. I want to generalize this to use [Braille ASCII](https://en.wikipedia.org/wiki/Braille_ASCII) aka [SimBraille](https://code.google.com/p/braille-font/downloads/detail?name=SimBraille.ttf) to transform any image to something that can be felt.

#### why

Sometimes it's easier to do things as a proof of concept. For example, to this day, I still use pages and preview to do all of my "photoshopping." It's easy and I'm familiar with it. Is the quality the best? No, but it's as good as I want it to be.

Still, I think this idea is worth delving into because it would be fun to get to know the python image processing library and also be able to render these images that are meant to be felt. It could be a bastardization of Braille, but it could also provide a new use for it just like ASCII art. Who knows.

##### Steps

1. pull in image and determine its size
2. process image 
  a. make black and white (not greyscale)
  b. divide into closest rectangle that can be composed of 2x3 rectangles
  c. pixelate the black and white image
  d. reference pixel mappings of braille characters
3. output
  a. braille ascii
  b. image of braille ascii
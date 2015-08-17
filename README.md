# ntbdth

This is a birthday gift I crafted for Nick this summer. It's a two week treasure hunt designed to have one clue per day. Half of them are virtual and half are in real life. I worked with his family and friends to bring this to life. I also had a great deal of help from some friends I made while interning at Uber, so I cannot thank everyone who helped pull this off enough.

I mean, you simply can't compete with friends who are willing to kick off the hunt by putting the very first clue in a bottle and slipping it into the arms of the participant midway through the night.

# Quest List

#### Language Decoding

In middle school, my friend Jackie introduced me to a secret language she and a friend came up with in lower school. I was pretty bored in our version of linear algebra one day, so I decided to resurrect the language. I had forgotten some of the letters, so I redesigned it hoping to stay as true to the original as possible. The clue was written in this "language."

#### In the Game

I lent Nick my GBA SP for the summer. Pokemon LeafGreen. The clue is literally in the game cartriage rather than in the virtual realm of the game. 

I drew inspiration for this from a cartoon I watched when I was a kid. There was some sort of secret recipe and it was hidden IN a computer. Physically. Shame I can't remember the show.

#### The Letter

I wrote a ton of letters this summer to Nick. If I had been thinking ahead, I would have put a clue in plain text in a letter in early July, but alas, I was last minute with this as per usual. I wanted to incorporate those letters into the hunt somehow though. Counting words in those letters is how I decided to do that.

#### Song Lyrics

The only clue is a three column CSV.
1. string
2. single digit
3. integer from 0-59

What might this be? Well, concatenated properly with [youtube](https://youtu.be/), you wind up with one song lyric per entry. Then unscramble the first letters to make a word. It was fun in 2nd grade and it's still fun now.

#### Loopback 1

This was an okay clue. I couldn't really come up with two sentences that made sense, so this one was a matter of not overthinking it. The answer was given in plain text.

#### Folder Maze

This one wasn't me, but just a brilliant idea from Nick's childhood.

More information on this to come with the permission of its creator.

#### Face the Music

Straight forward and a good break before the challenges got intense. 

Given: audio file with five notes spelling out "faded." Solution: Use a guitar tuner to get the letters.

The fun part was writing the code to come up with a list of English words only consisting of the letters A-G. Turns out, there aren't all that many. So much for disguising secret messages in musical notation.

#### Eat Your Way to a Solution

Also not mine. A twist on classic hangman.

More on where the idea came from and how the quote was chosen to come with the permission of this quest's creator.

#### Street Signs

Given locations all over Nick's hometown, clues lead from one place to the other.

This could not have been done without a childhood friend of Nick's. Thank you!!

Extensions of this would be to make a mobile app when fed a .kml file or individual coordinates, a geofence around the area is created. In order, once the participant steps into the geofence and the next clue pops up. Next time I have time to explore android stuff, this is what I'll be starting with :)

#### Braille Art

ASCII Characters -> SimBraille

#### Commandline Adventure

#### Loopback 2

#### House Photo Clues

#### QR Code

# Blog

I'm sure a github readme is NOT where this belongs, but that's just fine. Perhaps I'll actually get a blog or something at some point, but for now this will do.

There was a hiccup early on. Clues are not to be thought of as unimportant. I almost provided a test reference for *The Letter* quest, but I was just too tired to put it together. It turns out I had made some mistakes in my code too. One can never test too thoroughly. Even though 'going into production' in this case is super low risk because it's supposed to be fun, it always feels pretty crappy when it doesn't work as expected.

I should have put logging in earlier. I thought it would be super difficult but turns out it's really easy. Now all I have to do is `$ heroku logs | grep ATTEMPT` and I have all of the information I need. Lesson learned: don't knock it til you try it.



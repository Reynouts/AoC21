# AoC21

[![AUTO-README](https://github.com/Reynouts/AoC21/actions/workflows/readme.yml/badge.svg?branch=master)](https://github.com/Reynouts/AoC21/actions/workflows/readme.yml)

## [--- Day 1: Sonar Sweep ---](http://adventofcode.com/2021/day/1)
We are back! Easy first day. Second part had something to do with
the sum of a sliding window and compare it with the next. The inner elements
are constant, so you only have to compare the one going out of the window, with
the one entering the window.

I challenged my first year students to make this puzzle too in Java.
They haven't got a lot of tools in their toolbox, but they managed to
solve it! Nice work.

## [--- Day 2: Dive! ---](http://adventofcode.com/2021/day/2)
Another easy one, with classic AoC instructions. This time involving a
submarine. Tried to make it generic making a dictionary mapping from 
instruction to function. Probably a lot harder to understand than the
easy solution with some duplicate code. Let's see if this submarine
manual will return in later puzzles!

## [--- Day 3: Binary Diagnostic ---](http://adventofcode.com/2021/day/3)
Needed to refresh some numpy knowledge for this one. Had to use my lunchbreak
to solve the second part, because I didn't have enough time in the morning
before work. Took it quite literally and squeezed in some recursion to shrink
the data matrix without any problems. I guess it was a straightforward puzzle,
without the need to optimize anything. 

But this is mostly the case in the first days and suddenly
the compelxity explodes! For now, I am really happy with the amount of time
I need to invest in the puzzles to solve them. There is enough room to improve
your code if you have the time, but it is not a necessity.

## [--- Day 4: Giant Squid ---](http://adventofcode.com/2021/day/4)
Just had some limited time this weekend to solve the puzzles. In this puzzle
some numpy skills would be very beneficial, but I am not fluent enough with
the module to use it easily and I didn't have stable internet access, so I 
couldn't use it in full advantage. This made it quite a bit harder, but it did work out.


## [--- Day 5: Hydrothermal Venture ---](http://adventofcode.com/2021/day/5)
Puzzle of today: get all points on a line on a grid. Count all overlapping lines
in the grid. Some juggling with y=ax+b. Glad I could finish the puzzles within the
day!

## [--- Day 6: Lanternfish ---](http://adventofcode.com/2021/day/6)
The population of Laternfish is growing * growing. For part two a naive "simulate
every fish in the population"-way wouldn't cut it. So I used "bins" for the 9 types/
ages of the fishes and used a deque as datastructure to handle to needed rotation.
This resulted in a quick execution time and low space requirement.

Also I added a simple workflow to this repository to automatically decorate this
readme file with the correct names of the days and links to the puzzle. Just to get
a python script working in workflow.

## [--- Day 7: The Treachery of Whales ---](http://adventofcode.com/2021/day/7)
Finding a minimum in a search space. Tried to be smart and calculated the median and do
a left/right search for those points and see if it found a better solution. Turned out
the median is already optimal for part 1.
For part 2 I started from the average instead of the median, but didn't no if it would
work for every input, so just rewrote it to brute-force, which is a bit safer maybe and
also less code. And with this size of input it doesn't matter, brute-forcing both parts
are quick and give you the correct answer. So less reason to bother about it..

## [--- Day 8: Seven Segment Search ---](http://adventofcode.com/2021/day/8)
Quite a difficult puzzle to understand at first for me (except for part1). I started trying 
decoding all the segments itself (so: what letter should be on the top line, etc), but got 
some headache to solve it (I guess it is possible this way) and after work looked again and 
found out I didn't need that information to answer the question and it was a lot easier to 
eliminate and just compare the set of letters.

I've seen some very nice and clean solutions, but mine isn't one of them! No time to refactor
or overthink this. 16 stars and counting!


## [--- Day 9: Smoke Basin ---](http://adventofcode.com/2021/day/9)
Classic AoC puzzle: reading in a grid, checking neighbours and do something like a floodfill 
algorithm. Unfortunately I don't have enough time to really elaborate on problems, coding
style, performance and stuff like that like in earlier years. But happy to have some time
to solve the problems.

Note to self: make a library for this kind of stuff, think I coded this 20 times before for AoC.

## [--- Day 10: Syntax Scoring ---](http://adventofcode.com/2021/day/10)
Parse opening and closing symbols! Checking if the given "code" is incorrect and doing some
scoring. Tried to solve it quickly before going to work, but ended up with a bug that
I couldn't fix in time. So had to wait till lunch to get that out of my code. I forgot to
strip the newline characters with reading my file, which I caught in the first part of the
puzzle, but forgot in a letter if-statement. Took a while before I spotted that one.

## [--- Day 11: Dumbo Octopus ---](http://adventofcode.com/2021/day/11)
First kind of Game of Life puzzle of the year! Always fun and made me put some helpers
in my AoC package (reading grid and getting neighbours). Was expecting a harder second
part, but you could still simulate it and get the right answer (at least with my input)

## [--- Day 12: Passage Pathing ---](http://adventofcode.com/2021/day/12)
Today was also straight forward (just use a tree traversal method to get all paths) and
some extra datastructure and conditions to get the second part, but again quick enough
to get the answer for part 2! Usually the weekend puzzles are quite a bit harder, but
this time the first 12 days are all relatively easy. Maybe we will get a very steep curve
next week.. Let's see. I kinda like this small time investment, without too much braindraining
math puzzles.

## [--- Day 13: Transparent Origami ---](http://adventofcode.com/2021/day/13)
Folding a grid, until some characters appear! The pixel characters come back every now and
then in Advent of Code. Some people made patterns for every pixel character and use "pattern"
recognition to solve this automation step. The last time I wanted to use some OCR to automate it.
Something like using a hammer to kill a fly, but seemed fun nevertheless.

So this time I used opencv with pytesseract to do the OCR. Of course this doesn't work out of the
box, because it are really small "pictures" (only 5x5 pixels, but you never know what it will be
next time!). So I upscale the image a lot and add some filter to smooth the edges. This way tesseract
can do its job. Took some fiddling, but validated it with 3 other inputs. 

Fun stuff!

![Generated output picture](day13.png)

## [--- Day 14: Extended Polymerization ---](http://adventofcode.com/2021/day/14)
A string which grows so quickly, your memory won't survive this one.

Finally a brute-force na??ve solution won't cut it for part two. After some minutes observing the output, I couldn't 
figure out a pattern which I could use and needed to come up with a solution the programmers-way. Of course a dictionary 
provided the right datastructure to keep track of the pairs that were present in the string. Just some fiddling with 
counting the letters after it: you should counter the fact that the individual start and end letters are not in two 
pairs, all the other occurences of letters are in two pairs.


## [--- Day 15: Chiton ---](http://adventofcode.com/2021/day/15)
Pathfinding with Dijkstra! Like the Game Of Life and BFS/DFS puzzles, each year there is a
pathfinding puzzles with weighted edges. This time A* is not really necessary, because you always
move from one corner to the oppossite corner, so Dijkstra will do. But I just reused a A* implementation
I made some time ago (and made it fit to the puzzle..). Still not generic enough for real graphs (just grids).

Part two needed some extension of the given grid, which took me a bit too long. In retrospect I should have used numpy
for this, which makes it really easy. I moved some of my methods to my aoc "library", but I should refactor that, extend
it and generalise it to make it really reusable for new puzzles. But aoc needs to be fun, so I postpone that last part
until further notice...

Most unhappy with my code this day, but "real" work needs to be done before Christmas, so no time to be too picky.

## [--- Day 16: Packet Decoder ---](http://adventofcode.com/2021/day/16)
Is this the new IntCodeComputer that we will be building this year? If so: I will need to refactor this really
thoroughly! Became a big mess, after I rewrote it all to figure out were my bugs came from. I could not figure it out,
but eventually I found out my hex to binary method threw away leading zero's (of course, why wouldn't you?), which 
screws up the whole chain. And my input resulted in a case with a leadning zero. Fortunately there was one small 
testcase in the puzzle which failed (due to the same problem). But before I found out that was the problem, I discarded
my whole program multiple times.

Well, now it works, but really bad code. So please, don't come back in later days!

## [--- Day 17: Trick Shot ---](http://adventofcode.com/2021/day/17)
Easy day, which reminded me of the old DOS game "Gorillas" made in Q-Basic which I played a lot on my father's IBM
AT 5170. Aim and shoot your banana!

[![Gorillas](https://i.ytimg.com/vi/UDc3ZEKl-Wc/hqdefault.jpg)](https://www.youtube.com/watch?v=UDc3ZEKl-Wc)

For todays puzzle you needed to find the angle which hits a target box and gets as high as possible. Just brute force
this within the rules. The only part which requires some extra thinking is how to setup the ranges to make it work for
every scenario and don't let it loop too long. 

I guess this easy puzzle will lead us to a big time investment this weekend... maybe a sequel on day 16 (still not
refactored that one..)

## [--- Day 18: Snailfish ---](http://adventofcode.com/2021/day/18)
Reading of this puzzle took more time than the average coding time of last days, it was a tough one to get through.
A binary tree would be a useful datastructure to solve this "nested" snailfishes problem, but I didn't bother and didn't
even want to use a list. I just did string manipulations to keep track of the "reduced snailtrail" and juggled a bit 
with the digits. It resulted in ugly code (man.. did I really commit this code to a public repo...?), but it was quite 
good for debugging and seeing what happened.

For part 2 I made some weird mistake, which I thought had something to do with my big explode method. After getting some
extra testcases from Roland, I figured out I made a dumb error in calculating the maximum magnitude for all pairs. Well,
at least I solved it within the day!

Definitely the puzzle which took me the most time, but fortunately not too difficult to solve. Happy days! 

## [--- Day 19: Beacon Scanner ---](http://adventofcode.com/2021/day/19)
That was a tough one for me! Took me from 10pm 4 hours straight on and I already tried some things earlier this day. 
Well, just finished in time for the next puzzle. Didn't want to give up on my goal to solve every puzzle within the day
(or 24 hours after release..). 

I followed a path which I wasn't sure it would work, so I debugged a lot and after a while I threw it away and started 
again from scratch. To see which (reoriented) scanner matched another scanner, I check all the distances between all 
the points from scanner 1 to scanner 2. If there are 12 points exactly the same distance away (defined by the puzzle's
rules), we (probably) have a match and that is immediately the translation vector for the points (and the scanner). I
coded the orientation part first quite "hardcoded", but refactored it to a cleaner (but a more difficult to understand) 
solution.

After that I merge the points from scanner 2 to scanner 1. Rinse and repeat until all scanners are in the merged
scanner. The amount of beacons in the merged scanner is the answer for part 1. Part 2 was was easy this way, because I 
already knew to location of the scanners relative to the first scanner by this method.

Advent of Code takes my sleep!!

## [--- Day 20: Trench Map ---](http://adventofcode.com/2021/day/20)
Easy evolving grid with one "gotcha": the outer cells can change throughout the evolution. So you need to keep track of
the default outer value and after that it's easy. There wasn't a testcase which described this, so it was hard to know
what was going on at first, also because of the lack of testcases in the example. But I guess that was part of the fun
for this day.

## [--- Day 21: Dirac Dice ---](http://adventofcode.com/2021/day/21)
Fun little dice game, which you need some smart grouping of the problem to solve it or some caching. I used both for 
part two. Eventually I didn't need caching because I group the three dice rolls in one and multiply the paths with
the amount of possibilities in this group, which results in a 18s runtime without caching and around 40ms runtime with
caching (lru vs own dict doesn't matter that much).

## [--- Day 22: Reactor Reboot ---](http://adventofcode.com/2021/day/22)
Difficulty increases this day! We need to find intersections of cubes and try to keep track of which points are on (or
turned off again). There are big cubes, small cubes and I don't know how many times they could overlap. First intu??tion
was to subtract the intersection off-cube from the on-cube by subdividing the on-cube in smaller cubes and "delete" the
intersecting cubes, but this became hairy quite fast. So I "layered" the intersecting cubes, to phase out the on (or 
off cube). This way no subdividing is necessary. Definately not an easy one.

## [--- Day 23: Amphipod ---](http://adventofcode.com/2021/day/23)
Loved this one, but didn't solve it programmatically (yet). Just implemented it as a console game, keep track of the 
score and previous states (to easy undo) and played around to get the right answers! Easy this way, progamatically
probably a bit trickier to get a pathfinding algorithm with constaints. Maybe later.. but I feel more for making this
console game more complete :-D

## [--- Day 24: Arithmetic Logic Unit ---](http://adventofcode.com/2021/day/24)
Implemented the operations and tried to find some logic in the output, but that didn't went anywhere. Decomposed the
input and made a bit more sense, but still nowhere near an answer. But wait, there are not 14 different "patterns" but
only 2 with different constants. Hmm, there is something in that. Don't feel like it to assemble this by hand in excel.

-- revisited on day 25 -- Unfortunately couldn't finish it within 24 hours. So I didn't complete my objective on this 
day. But this can be done with hand and paper. Didn't feel to do it that way and went down the rabbit hole and made a
more "generic" solution (probably won't work on all inputs, not sure). 

## [--- Day 25: Sea Cucumber ---](http://adventofcode.com/2021/day/25)
Nice classic AoC puzzle to end this year. Loved this one, but didn't spend too much time on it, cause I had to do day
24 still. This was a nice one for a visualisation! But have to put that on the list again for
next year. 

It was a great year! Easy start in the first weeks and from day 19 a shift, which cost me a lot of time and
sleep. Enjoyed the stories, classic AoC puzzles, braindrain reading, struggling with debugging, discussions about the
most performant code in the first days (and really caring about it in later days) and the private leaderboards (because
I can't compete with the global leaderboard; I won't set an alarm anymore, because I know I'm too slow.)

See you in 2022!!

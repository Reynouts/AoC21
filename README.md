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

--- Day 11: ** Dumbo Octopus ---
You enter a large cavern full of rare bioluminescent
dumbo octopuses
! They seem to not like the Christmas lights on your submarine, so you turn them off for now.**
There are 100
octopuses
arranged neatly in a 10 by 10 grid.** Each octopus slowly gains
energy
over time and
flashes
brightly for a moment when its energy is full.** Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.**
Each octopus has an
energy level
- your submarine can remotely measure the energy level of each octopus (your puzzle input).** For example: **
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
The energy level of each octopus is a value between
0
and
9
.** Here, the top-left octopus has an energy level of
5
, the bottom-right one has an energy level of
6
, and so on.**
You can model the energy levels and flashes of light in
steps
.** During a single step, the following occurs: **
First, the energy level of each octopus increases by
1
.**
Then, any octopus with an energy level greater than
9
flashes
.** This increases the energy level of all adjacent octopuses by
1
, including octopuses that are diagonally adjacent.** If this causes an octopus to have an energy level greater than
9
, it
also flashes
.** This process continues as long as new octopuses keep having their energy level increased beyond
9
.** (An octopus can only flash
at most once per step
.**)
Finally, any octopus that flashed during this step has its energy level set to
0
, as it used all of its energy to flash.**
Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.** Consider the middle octopus with
1
energy in this situation: **
Before any steps: **
11111
19991
19191
19991
11111

After step 1: **
34543
4
000
4
5
000
5
4
000
4
34543

After step 2: **
45654
51115
61116
51115
45654
An octopus is
highlighted
when it flashed during the given step.**
Here is how the larger example above progresses: **
Before any steps: **
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

After step 1: **
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637

After step 2: **
88
0
7476555
5
0
89
0
87
0
54
85978896
0
8
84857696
00
87
00
9
0
88
00
66
000
88989
68
0000
5943
000000
7456
9
000000
876
87
0000
6848

After step 3: **
00
5
0
9
00
866
85
00
8
00
575
99
000000
39
97
000000
41
9935
0
8
00
63
77123
00000
791125
000
9
221113
0000
0
421125
000
00
21119
000
After step 4: **
2263
0
31977
0
923
0
31697
00
3222115
0
00
41111163
00
76191174
00
53411122
00
4236112
0
5532241122
1532247211
113223
0
211

After step 5: **
4484144
000
2
0
44144
000
2253333493
1152333274
11873
0
3285
1164633233
1153472231
6643352233
2643358322
2243341322

After step 6: **
5595255111
3155255222
33644446
0
5
2263444496
2298414396
2275744344
2264583342
7754463344
3754469433
3354452433

After step 7: **
67
0
7366222
4377366333
4475555827
34966557
0
9
35
00
6256
0
9
35
0
9955566
3486694453
8865585555
486558
0
644
4465574644

After step 8: **
7818477333
5488477444
5697666949
46
0
876683
0
473494673
0
474
00
97688
69
0000
7564
000000
9666
8
00000
4755
68
0000
7755

After step 9: **
9
0
6
0000
644
78
00000
976
69
000000
8
0
584
00000
82
5858
0000
93
69624
00000
8
0
2125
000
9
222113
000
9
9111128
0
97
7911119976

After step 10: **
0
481112976
00
31112
00
9
00
411125
0
4
00
811114
0
6
00
991113
0
6
00
93511233
0
44236113
0
553225235
0
0
53225
0
6
00
00
3224
0000
After step 10, there have been a total of
204
flashes.** Fast forwarding, here is the same configuration every 10 steps: **
After step 20: **
3936556452
56865568
0
6
449655569
0
444865558
0
445686557
0
568
00
86577
7
00000
9896
0000000
344
6
000000
364
46
0000
9543

After step 30: **
0
643334118
4253334611
3374333458
2225333337
2229333338
2276733333
2754574565
5544458511
9444447111
7944446119

After step 40: **
6211111981
0
421111119
00
42111115
000
3111115
000
3111116
00
65611111
0
532351111
3322234597
2222222976
2222222762

After step 50: **
9655556447
48655568
0
5
448655569
0
445865558
0
457486557
0
57
000
86566
6
00000
9887
8
000000
533
68
00000
633
568
0000
538

After step 60: **
25333342
00
274333464
0
2264333458
2225333337
2225333338
2287833333
3854573455
1854458611
1175447111
1115446111

After step 70: **
8211111164
0
421111166
00
42111114
000
4211115
0000
211116
00
65611111
0
532351111
7322235117
5722223475
4572222754

After step 80: **
1755555697
59655556
0
9
448655568
0
445865558
0
457
0
86557
0
57
000
86566
7
00000
8666
0000000
99
0
0000000
8
00
0000000000
After step 90: **
7433333522
2643333522
2264333458
2226433337
2222433338
2287833333
2854573333
4854458333
3387779333
3333333333

After step 100: **
0
397666866
0
749766918
00
53976933
000
4297822
000
4229892
00
53222877
0
532222966
9322228966
7922286866
6789998766
After 100 steps, there have been a total of
1656
flashes.**
Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps.**
How many total flashes are there after 100 steps?

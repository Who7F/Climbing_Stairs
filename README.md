#Climbing Stairs
#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#1 <= n <= 45

So its the fibonacci sequence with an off set of one.

The first 6 numbers are 1,2,3,5,8,13, and not 1,1,2,3,5,8(fibonacci)

But why? Okay I know why.

1st sets:

1

2nd sets:

11

2

3rd sets: 

1 1 1

1 2

21

4th is:

append 1, to each list in the 3rd set

plus append 2 to each list in the 2nd set

Adds up to: 5 lists unique that all sum to 4 

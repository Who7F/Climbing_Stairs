#Climbing Stairs
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#1 <= n <= 45
import time


class solution:
    def __init__(self):
        pass


        
    def climbStairs(self, n):
        fib = [
            1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,
            4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
            196418, 317811, 514229, 832040, 1346269, 2178309, 3524578,
            5702887, 9227465, 14930352, 24157817, 39088169,63245986,
            102334155, 165580141, 267914296, 433494437, 701408733,
            1134903170, 1836311903, 2971215073, 4807526976,7778742049,
            12586269025, 20365011074
            ]

        return fib[n]

  

def main():
    print('Climbing Stairs tests\n')
    print('Time Module imported in order to slow the test down\n\n')
    #f = solution()

    print('Test One:  ', end = ' ')
    time.sleep(0.5)
    if solution().climbStairs(2) == 2:
        print('Pass')
    else:
        print('Fail')
        
    print('Test Two:  ', end = ' ')
    time.sleep(0.5)
    if solution().climbStairs(3) == 3:
        print('Pass')
    else:
        print('Fail')
        
    print('Test Three:', end = ' ')
    time.sleep(0.5)
    if solution().climbStairs(1) == 1:
        print('Pass')
    else:
        print('Fail')

    print('Test Fore: ', end = ' ')
    time.sleep(0.5)
    if solution().climbStairs(45) == 1836311903:
        print('Pass')
    else:
        print('Fail')


if __name__== '__main__':
    main()

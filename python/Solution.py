#Climbing Stairs
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#1 <= n <= 45

import time

class solution:
    
    def climbStairs(self :type, n :int) -> int:#Yeah. What type is self
        stepArry :list = [1, 0]; swtich :int = 0
        
        for _ in range(n):
            swtich = 1 if swtich == 0 else 0
            stepArry[swtich] = sum(stepArry)

        return stepArry[swtich]

  

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

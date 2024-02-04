#Climbing Stairs
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#1 <= n <= 45

class solution:
    def __init__(self, n):
        self.stepsArray = [1 for _ in range(n)]
        self.len = n
        self.pointer = 0

    def printSteps(self) -> type:
        return type(type(self.stepsArray))
        
    def climbStairs(self, n):
        self.stepsArray = [0 for _ in self.stepsArray]
        self.stepsArray[self.pointer] = 1
        return self.continuingClimbStairs(n)

    def continuingClimbStairs(self, n):
        for _ in range(n):
            #self.pointer = self.pointer +1 if self.pointer < self.len -1 else 0
            #Just to ugly 
            if self.pointer < self.len -1:
                self.pointer += 1
            else:
                self.pointer = 0
            self.stepsArray[self.pointer] = sum(self.stepsArray)
        return self.stepsArray[self.pointer]

def main():
    print('Climbing Stairs tests\n')
    f = solution(2)
    #print(f.printSteps())
    
    print('Test One:  ', end = ' ')
    
    if f.climbStairs(2) == 2:
        print('Pass')
    else:
        print('Fail')
        
    print('Test Two:  ', end = ' ')
    
    if f.climbStairs(3) == 3:
        print('Pass')
    else:
        print('Fail')
        
    print('Test Three:', end = ' ')
    
    if f.climbStairs(1) == 1:
        print('Pass')
    else:
        print('Fail')

    print('Test Fore: ', end = ' ')
    
    if f.climbStairs(45) == 1836311903:
        print('Pass')
    else:
        print('Fail')

if __name__== '__main__':
    main()

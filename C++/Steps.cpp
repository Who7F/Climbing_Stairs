// Steps.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Solution.h"

int main()
{
    Solution f;
    std::cout << "Running tests.!\n\n\n";
    
    std::cout << "Testing input  2: ";
    if (f.climbStairs(2) == 2) {
        std::cout << "Pass\n\n";
    }
    std::cout << "Testing input  3: ";
    if (f.climbStairs(3) == 3) {
        std::cout << "Pass\n\n";
    }
    std::cout << "Testing input  4: ";
    if (f.climbStairs(4) == 5) {
        std::cout << "Pass\n\n";
    }
    std::cout << "Testing input  1: ";
    if (f.climbStairs(1) == 1) {
        std::cout << "Pass\n\n";
    }
    std::cout << "Testing input 45: ";
    if (f.climbStairs(45) == 1836311903) {
        std::cout << "Pass\n\n";
    }
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

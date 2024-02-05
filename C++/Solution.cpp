#include "Solution.h"

int Solution::climbStairs(int n) {
	int array[2] = { 1, 0 };
	int swtich = 0;
	for (int _ = 0; _ < n; _++) {
		if (swtich == 1){
			swtich = 0;
		}
		else {
			swtich = 1;
		}
		array[swtich] = array[0] + array[1];
	}
	return array[swtich];
}

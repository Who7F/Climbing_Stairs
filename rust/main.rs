pub struct Solution;

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
		let mut array: [i32; 2] = [0, 1];
		let mut switch: i32 = 0;
		for _ in 0..n+1{
			if switch == 1{
				switch = 0;
			}else{
				switch =1;
			}
			array[switch as usize] = array.iter().sum()
		} 
        array[switch as usize]
    }
}



fn main() {
    println!("Running Tests");
	assert_eq!(Solution::climb_stairs(2), 2);
	assert_eq!(Solution::climb_stairs(3), 3);
	assert_eq!(Solution::climb_stairs(6), 13);
	assert_eq!(Solution::climb_stairs(1), 1);
	assert_eq!(Solution::climb_stairs(45), 1836311903);
	println!("Tests Complete");
}

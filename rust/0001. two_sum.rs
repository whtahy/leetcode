use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hm = HashMap::new();

        for (i, x) in nums.iter().enumerate() {
            let complement = target - x;
            if hm.contains_key(&complement) {
                return vec![i as i32, hm[&complement]];
            } else {
                hm.insert(x, i as i32);
            }
        }

        panic!()
    }
}

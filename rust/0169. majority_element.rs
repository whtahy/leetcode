// Boyer-Moore majority voting
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut m = 0;
        let mut i = 0;

        for x in nums {
            if i == 0 {
                m = x;
                i = 1;
            } else if m == x {
                i += 1
            } else {
                i -= 1
            }
        }

        m
    }
}

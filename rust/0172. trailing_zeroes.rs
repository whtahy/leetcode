impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        let mut z = 0;
        let mut x = n;
        while x > 0 {
            x /= 5;
            z += x;
        }

        z
    }
}

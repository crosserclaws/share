fn main() {
    case_non_overflow();
    case_overflow();
}

fn sum(integers: &[u32]) -> Option<u32> {
    let mut s: u32 = 0;
    for x in integers {
        let y = s.checked_add(*x);
        if y.is_none() {
            return y;
        }
        s = y.unwrap();
    }
    Some(s)
}

fn case_non_overflow() {
    let case = [1, 2, 3];
    let res = sum(&case);
    println!("Sum of {:?} is {:?}", case, res);
}

fn case_overflow() {
    let case = [1, 2, u32::MAX];
    let res = sum(&case);
    println!("Sum of {:?} is {:?}", case, res);
}

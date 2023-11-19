fn main() {
    let raw = [3, 2, 1, 1, 0];
    let mut array = raw.clone();
    bubble_sort(&mut array);
    println!("Bubble Sort: {:?} -> {:?}", raw, array);
}

fn bubble_sort<T: PartialOrd>(arr: &mut [T]) {
    for i in 0..(arr.len() - 1) {
        for j in 0..(arr.len() - i - 1) {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
            }
        }
    }
}

#[test]
fn test_vec() {
    let mut v = vec![3, 2, 1];
    bubble_sort(&mut v);
    assert_eq!(v, vec![1, 2, 3]);
}

#[test]
fn test_integer() {
    let mut array = [1, 0, -2, 3, -4];
    bubble_sort(&mut array);
    assert_eq!(array, [-4, -2, 0, 1, 3]);
}

#[test]
fn test_float() {
    let mut array = [1.1, 0.0, -2.2, f64::INFINITY, f64::NEG_INFINITY];
    bubble_sort(&mut array);
    assert_eq!(array, [f64::NEG_INFINITY, -2.2, 0.0, 1.1, f64::INFINITY]);
}

#[test]
fn test_str() {
    let mut array = ["abc", "aa", "aaa", "zz", "gg"];
    bubble_sort(&mut array);
    assert_eq!(array, ["aa", "aaa", "abc", "gg", "zz"]);
}

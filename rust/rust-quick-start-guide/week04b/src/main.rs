use std::fmt;
use std::fmt::Display;
use std::ops::Add;

#[derive(Copy, Clone, Debug)]
struct Vector {
    x: i32,
    y: i32,
}

impl Add for Vector {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

impl Display for Vector {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

fn adder<T: Add<Output = T> + Copy>(a: &T, b: &T) -> T {
    *a + *b
}


fn main() {
    let v1 = Vector { x: 1, y: 2 };
    let v2 = Vector { x: 2, y: 2 };
    println!("v1 + v2 = {v1} + {v2} = ?");
    println!("Add: {}", adder(&v1, &v2));
}

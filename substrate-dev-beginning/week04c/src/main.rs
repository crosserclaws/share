fn main() {
    let s = Square { edge: 2.0 };
    print_area(s);

    let c = Circle { radius: 2.0 };
    print_area(c);
}

fn print_area<T: Area + std::fmt::Debug>(shape: T) {
    println!("The area of shape {:?} is {}", shape, shape.area());
}

trait Area {
    fn area(&self) -> f64;
}

#[derive(Debug)]
struct Square {
    edge: f64,
}

impl Area for Square {
    fn area(&self) -> f64 {
        self.edge.powf(2.0)
    }
}

#[derive(Debug)]
struct Circle {
    radius: f64,
}

impl Area for Circle {
    fn area(&self) -> f64 {
        self.radius.powf(2.0) * std::f64::consts::PI
    }
}

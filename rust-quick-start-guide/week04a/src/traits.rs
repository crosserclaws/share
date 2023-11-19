trait Animal {
    fn greet(&self);
}

struct Bird {}
impl Animal for Bird {
    fn greet(&self) {
        println!("Bird says hi trait!");
    }
}

struct Cat {}
impl Animal for Cat {
    fn greet(&self) {
        println!("Cat says hi trait!");
    }
}

struct Dog {}
impl Animal for Dog {
    fn greet(&self) {
        println!("Dog says hi trait!");
    }
}

pub fn demo() {
    let b = Bird{};
    let c = Cat{};
    let d = Dog{};
    let v: Vec<&dyn Animal> = vec![&b, &c, &d];
    for a in &v {
        a.greet();
    }
}

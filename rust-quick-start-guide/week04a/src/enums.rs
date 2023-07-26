enum Animal {
    Bird(Bird),
    Cat(Cat),
    Dog(Dog),
}

impl Animal {
    fn greet(&self) {
        match self {
            Animal::Bird(b) => b.greet(),
            Animal::Cat(c) => c.greet(),
            Animal::Dog(d) => d.greet(),
        }
    }
}

struct Bird {}
impl Bird {
    fn greet(&self) {
        println!("Bird says hi enum!");
    }
}

struct Cat {}
impl Cat {
    fn greet(&self) {
        println!("Cat says hi enum!");
    }
}

struct Dog {}
impl Dog {
    fn greet(&self) {
        println!("Dog says hi enum!");
    }
}

pub fn demo() {
    let b = Bird{};
    let c = Cat{};
    let d = Dog{};
    let v: Vec<Animal> = vec![Animal::Bird(b), Animal::Cat(c), Animal::Dog(d)];
    for a in &v {
        a.greet();
    }
}

fn main() {
    let red = TrafficLight::Red;
    print_traffic_time(red);

    let yellow = TrafficLight::Yellow;
    print_traffic_time(yellow);

    let green = TrafficLight::Green;
    print_traffic_time(green);
}

fn print_traffic_time(light: TrafficLight) {
    println!("{:?} light continues for {} seconds.", light, light.second());
}

trait Time {
    fn second(&self) -> u8;
}

#[derive(Debug)]
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

impl Time for TrafficLight {
    fn second(&self) -> u8 {
        match self {
            Self::Red => 60,
            Self::Yellow => 2,
            Self::Green => 90
        }
    }
}


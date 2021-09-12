#[derive(PartialEq, Debug)]
// Declare Car struct to describe vehicle with four named fields
struct Car {
    color: String,
    motor: Transmission,
    roof: bool,
    age: (String, u32),
}

#[derive(PartialEq, Debug)]
// Declare enum for Car transmission type
enum Transmission {
    Manual,
    SemiAuto,
    Automatic,
}

// Get the car quality by testing the value of the input argument
// - miles (u32)
// Create a tuple for the car quality with the age ("New" or "Used") and miles
// Return a tuple with the arrow `->` syntax
fn car_quality(miles: u32) -> (String, u32) {
    if miles > 0 {
        ("Used".to_string(), miles)
    } else {
        ("New".to_string(), 0)
    }
}

// Build a new "Car" using the values of four input arguments
// - color (String)
// - motor (Transmission enum)
// - roof (boolean, true if the car has closed roof)
// - miles (u32)
// Call the car_quality(miles) function to get the car age
// Return an instance of a "Car" struct with the arrow `->` syntax
fn car_factory(color: String, motor: Transmission, roof: bool, miles: u32) -> Car {
    Car {
        color: color,
        motor: motor,
        roof: roof,
        age: car_quality(miles),
    }
}

fn main() {
    let colors = ["Blue", "Green", "Red", "Silver"];

    // Initialize variables
    let mut index = 1;

    // Declare the car type and initial values
    let mut car: Car;
    let mut engine: Transmission;
    let mut miles = 1000; // Start used cars with 1,000 miles
    let roof = true; // convertible = false | hard top = true

    // Order 11 cars
    for order in 1..12 {
        // Set car transmission type
        engine = Transmission::Manual;

        // Order the cars, New are even numbers, Used are odd numbers
        if index % 2 != 0 {
            car = car_factory(colors[index].to_string(), engine, roof, miles);
        } else {
            car = car_factory(colors[0].to_string(), engine, roof, 0);
        }

        // Display car order details
        println!(
            "{}: {}, Closed roof, {:?}, {}, {} miles",
            order, car.age.0, car.motor, car.color, car.age.1
        );

        miles += 1000;
        index = (index + 1) % colors.len();
    }
}

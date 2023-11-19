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
    // Initialize a hash map for car orders
    // - Keys: New or Used, Values: integer
    // - Keys: Manual or Automatic, Values: integer
    use std::collections::HashMap;
    let mut orders: HashMap<String, u32> = HashMap::new();
    let (mut new_cars, mut used_cars) = (1, 1);
    let (mut manual, mut auto) = (1, 1);

    let colors = ["Blue", "Green", "Red", "Silver"];

    // Initialize variables
    let mut index = 0;

    // Declare the car type and initial values
    let mut car: Car;
    let mut engine: Transmission;
    let mut miles = 1000; // Start used cars with 1,000 miles
    let mut roof = true; // convertible = false | hard top = true

    // Order 11 cars
    for order in 1..12 {
        // Set car transmission type, make some roofs convertible
        // Check order number, set engine type, fix syntax
        // If order % 3 equals 0, engine is "Automatic"
        // If order % 2 equals 0, engine is "SemiAuto" | else, engine is "Manual"
        // When order % 3, swap roof type for fun!
        if order % 3 == 0 {
            engine = Transmission::Automatic;
            roof = !roof;
            orders.insert("Automatic".to_string(), auto);
            auto = auto + 1;
        } else if order % 2 == 0 {
            engine = Transmission::SemiAuto;
        } else {
            engine = Transmission::Manual;
            orders.insert("Manual".to_string(), manual);
            manual = manual + 1;
        }

        // Order the cars, New are even numbers, Used are odd numbers
        // Corrected code: Index into `colors` array, vary color for the orders
        if index % 2 != 0 {
            car = car_factory(colors[index].to_string(), engine, roof, 0);
            orders.insert("New".to_string(), new_cars);
            new_cars = new_cars + 1;
        } else {
            car = car_factory(colors[index].to_string(), engine, roof, miles);
            orders.insert("Used".to_string(), used_cars);
            used_cars = used_cars + 1;
        }

        // Display car order details by roof type and age of car
        if car.roof && car.age.1 > 0 {
            println!(
                "{}: {}, {:?}, Closed roof, {}, {} miles",
                order, car.age.0, car.motor, car.color, car.age.1
            );
        } else if car.roof && car.age.1 == 0 {
            println!(
                "{}: {}, {:?}, Closed roof, {}",
                order, car.age.0, car.motor, car.color
            );
        } else if !car.roof && car.age.1 > 0 {
            println!(
                "{}: {}, {:?}, Convertible, {}, {} miles",
                order, car.age.0, car.motor, car.color, car.age.1
            );
        } else {
            println!(
                "{}: {}, {:?}, Convertible, {}",
                order, car.age.0, car.motor, car.color
            );
        }

        miles += 1000;
        index = (index + 1) % colors.len();
    }
    // Display the hash map of car orders, show <K, V> pairs
    println!("\nCar orders: {:?}", orders);
}

pub mod nested;

#[allow(non_snake_case)]
pub fn print_a_to_Z() {
    for c in ('Z'..='a').rev() {
        print!("{}", c);
    }
    println!();
}

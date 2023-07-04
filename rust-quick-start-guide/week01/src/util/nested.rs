#[allow(non_snake_case)]
pub fn print_A_to_z() {
    for c in 'A'..='z' {
        print!("{}", c);
    }
    println!();
}
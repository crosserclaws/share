use std::time::Duration;

use chrono::Local;
use tokio::time;


#[tokio::main]
async fn main() {
    let mut interval = time::interval(Duration::from_secs(1));

    println!("{}", Local::now());
    interval.tick().await;
    println!("{}", Local::now());
    interval.tick().await;
    println!("{}", Local::now());
    interval.tick().await;
    println!("{}", Local::now());
}

use tokio::fs::File;
use tokio::io::AsyncReadExt;


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    do_read().await?;
    Ok(())
}

async fn do_read() -> Result<(), std::io::Error> {
    let mut file = File::open("target/foo.txt").await?;
    let mut content = String::new();
    let length = file.read_to_string(&mut content).await?;
    println!(r#"Content is {:#?}. The length is {}."#, content, length);
    Ok(())
}

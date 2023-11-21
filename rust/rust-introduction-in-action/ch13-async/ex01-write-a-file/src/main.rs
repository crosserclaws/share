use tokio::fs::File;
use tokio::io::AsyncWriteExt;


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    do_write().await?;
    Ok(())
}

async fn do_write() -> Result<(), std::io::Error> {
    let mut file = File::create("foo.txt").await?;
    file.write_all(b"Hello World").await?;
    Ok(())
}

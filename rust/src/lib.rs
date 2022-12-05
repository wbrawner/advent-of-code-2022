pub mod util {
    use std::{
        fs::File,
        io::{BufRead, BufReader},
    };

    pub fn read_input(name: &str) -> Result<Vec<String>, std::io::Error> {
        BufReader::new(File::open(format!("{}.txt", name))?)
            .lines()
            .collect()
    }
}

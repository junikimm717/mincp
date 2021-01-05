#[allow(unused_imports)]
use std::io::{BufWriter, Write, stdin, stdout};

#[derive(Default)]
struct Scanner {
    buffer: Vec<String>,
}

#[allow(dead_code)]
impl Scanner {
    fn next<T:std::str::FromStr> (&mut self) -> T {
        loop {
            if let Some(res) = self.buffer.pop() {
                return res.parse().ok().expect("fail");
            }
            let mut s = String::new();
            stdin().read_line(&mut s).expect("fail");
            self.buffer = s.split_whitespace().rev().map(String::from).collect();
        }
    }
}

#[allow(unused_variables)]
fn main() {
    let mut sc = Scanner::default();
    let mut out = BufWriter::new(stdout());
}

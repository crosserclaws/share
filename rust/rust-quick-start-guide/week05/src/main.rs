macro_rules! set {
    () => {
        std::collections::HashSet::new()
    };
    ($($x: expr), +) => {
        {
            let mut s = std::collections::HashSet::new();
            $( s.insert($x); )+
            s
        }
    }
}

macro_rules! eval {
    ($e: expr) => {
        eprintln!("Eval: {:?} = {:?}", stringify!($e), $e);
    }
}

fn main() {
    let my_set = set!(1, 2, 3);
    eval!(my_set);
}

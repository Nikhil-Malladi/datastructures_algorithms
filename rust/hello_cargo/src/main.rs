fn main() {
    let mut x=5;
    println!("the value of x is : {x}");
    x = 6;
    const Y: i32 = 6;
    println!("the value of x is : {x}");
    const NIKHIL: &str ="person";
    println!("{NIKHIL}");
    let z = add_two_numbers(x,Y);
    println!("{z}");
}

fn add_two_numbers(x: i32, y: i32) -> i32{
    let z = x+y;
    return z;
}
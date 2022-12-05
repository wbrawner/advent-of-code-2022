use rust::util::read_input;
use std::cmp::max;
use std::cmp::min;

fn part1(input: &Vec<String>) -> u32 {
    let mut overlapping = 0;
    for pair in input.iter() {
        let groups: Vec<Vec<u32>> = pair
            .split(",")
            .map(|group| {
                group
                    .split("-")
                    .map(|num| str::parse(num).expect("Invalid input"))
                    .collect()
            })
            .collect();
        let first = &groups[0];
        let second = &groups[1];
        if (first[0] <= second[0] && first[1] >= second[1])
            || (second[0] <= first[0] && second[1] >= first[1])
        {
            overlapping += 1;
        }
    }
    overlapping
}

fn part2(input: &Vec<String>) -> u32 {
    let mut overlapping = 0;
    for pair in input.iter() {
        let groups: Vec<Vec<u32>> = pair
            .split(",")
            .map(|group| {
                group
                    .split("-")
                    .map(|num| str::parse(num).expect("Invalid input"))
                    .collect()
            })
            .collect();
        let first = &groups[0];
        let second = &groups[1];
        let largest_start = max(first[0], second[0]);
        let smallest_end = min(first[1], second[1]);
        if (first[0] <= second[0] && first[1] >= second[1])
            || (second[0] <= first[0] && second[1] >= first[1])
            || largest_start <= smallest_end
        {
            overlapping += 1;
        }
    }
    overlapping
}

fn main() {
    let test_input = read_input("Day04_test").expect("Failed to open test input");
    assert_eq!(2, part1(&test_input));
    assert_eq!(4, part2(&test_input));

    let input = read_input("Day04").expect("Failed to open input");
    println!("{:?}", part1(&input));
    println!("{:?}", part2(&input));
}

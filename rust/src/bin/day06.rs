use rust::util::read_input;
use std::collections::{hash_map::RandomState, HashSet, VecDeque};

fn part1(input: &str) -> usize {
    let mut previous_three: VecDeque<char> = VecDeque::new();
    for (i, c) in input.char_indices() {
        if previous_three.len() < 3 {
            previous_three.push_back(c);
            continue;
        }

        let set: HashSet<&char, RandomState> = HashSet::from_iter(previous_three.iter());
        if previous_three.contains(&c) || set.len() < 3 {
            previous_three.pop_front();
            previous_three.push_back(c);
            continue;
        }

        return i + 1;
    }
    0
}

fn part2(input: &str) -> usize {
    let mut previous_three: VecDeque<char> = VecDeque::new();
    for (i, c) in input.char_indices() {
        if previous_three.len() < 13 {
            previous_three.push_back(c);
            continue;
        }

        let set: HashSet<&char, RandomState> = HashSet::from_iter(previous_three.iter());
        if previous_three.contains(&c) || set.len() < 13 {
            previous_three.pop_front();
            previous_three.push_back(c);
            continue;
        }

        return i + 1;
    }
    0
}

fn main() {
    let test_input = read_input("Day06_test").expect("Failed to open test input");
    let test_input_first = test_input.first().expect("Received empty input");
    assert_eq!(7, part1(&test_input_first));
    assert_eq!(19, part2(&test_input_first));

    let input = read_input("Day06").expect("Failed to open input");
    let input_first = input.first().expect("Received empty input");
    println!("{:?}", part1(&input_first));
    println!("{:?}", part2(&input_first));
}

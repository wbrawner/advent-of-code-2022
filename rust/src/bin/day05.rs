use rust::util::read_input;
use std::collections::VecDeque;

fn build_stacks(input: &Vec<String>) -> Vec<VecDeque<char>> {
    let mut stacks: Vec<VecDeque<char>> = vec![];
    input
        .iter()
        .take_while(|line| !line.trim_start().starts_with("1"))
        .for_each(|line| {
            line.char_indices().for_each(|(i, c)| {
                if i == 0 || (i - 1) % 4 != 0 {
                    return;
                }
                let stack_index = (i - 1) / 4;
                if stack_index >= stacks.len() {
                    let mut stack = VecDeque::new();
                    if c != ' ' {
                        stack.push_front(c);
                    }
                    stacks.push(stack);
                } else {
                    if c != ' ' {
                        stacks[stack_index].push_front(c);
                    }
                }
            })
        });
    stacks
}

fn part1(input: &Vec<String>) -> String {
    let mut stacks = build_stacks(&input);
    input
        .iter()
        .skip_while(|line| !line.starts_with("move"))
        .for_each(
            |line| match line.split(' ').collect::<Vec<&str>>().as_slice() {
                [_, amount_str, _, from_index_str, _, to_index_str] => {
                    let from_index = usize::from_str_radix(from_index_str, 10)
                        .expect("failed to parse from_index")
                        - 1;
                    let to_index = usize::from_str_radix(to_index_str, 10)
                        .expect("failed to parse to_index")
                        - 1;
                    let amount =
                        usize::from_str_radix(amount_str, 10).expect("failed to parse amount");
                    for _ in 0..amount {
                        let from = stacks[from_index]
                            .pop_back()
                            .expect("invalid instruction: attempted to move from empty stack");
                        let to = &mut stacks[to_index];
                        to.push_back(from);
                    }
                }
                _ => panic!("invalid instruction"),
            },
        );
    stacks
        .iter()
        .map(|stack| stack.back().unwrap_or(&' '))
        .collect::<String>()
}

fn part2(input: &Vec<String>) -> String {
    let mut stacks = build_stacks(&input);
    input
        .iter()
        .skip_while(|line| !line.starts_with("move"))
        .for_each(
            |line| match line.split(' ').collect::<Vec<&str>>().as_slice() {
                [_, amount_str, _, from_index_str, _, to_index_str] => {
                    let from_index = usize::from_str_radix(from_index_str, 10)
                        .expect("failed to parse from_index")
                        - 1;
                    let to_index = usize::from_str_radix(to_index_str, 10)
                        .expect("failed to parse to_index")
                        - 1;
                    let amount =
                        usize::from_str_radix(amount_str, 10).expect("failed to parse amount");
                    let amount_index = stacks[from_index].len() - amount;
                    let from = stacks[from_index].split_off(amount_index);
                    let to = &mut stacks[to_index];
                    for item in from {
                        to.push_back(item);
                    }
                }
                _ => panic!("invalid instruction"),
            },
        );
    stacks
        .iter()
        .map(|stack| stack.back().unwrap_or(&' '))
        .collect::<String>()
}

fn main() {
    let test_input = read_input("Day05_test").expect("Failed to open test input");
    assert_eq!("CMZ", part1(&test_input));
    assert_eq!("MCD", part2(&test_input));

    let input = read_input("Day05").expect("Failed to open input");
    println!("{:?}", part1(&input));
    println!("{:?}", part2(&input));
}

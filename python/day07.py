#!/usr/bin/env python3

from dataclasses import dataclass, field
from sys import maxsize
from util import read_input


@dataclass
class File:
    name: str
    size: int

    def __hash__(self):
        return hash('file' + self.name)


@dataclass
class Directory:
    name: str
    children: set = field(default_factory=set)

    def __hash__(self):
        return hash('dir' + self.name)


def build_dir_tree(commands):
    root = Directory('/')
    current_path = [root]

    for line in commands:
        if line.startswith("$"):
            command = line.split(' ')
            if command[1] == 'cd':
                name = command[2].strip()
                if name == '/':
                    current_path = [root]
                elif name == '..':
                    if len(current_path) > 0:
                        current_path.pop()
                else:
                    for child in current_path[-1].children:
                        if child.name == name:
                            current_path.append(child)
                            break
            elif command[1] == 'ls':
                pass
        elif line.startswith("dir"):
            name = line.split(' ')[1].strip()
            current_path[-1].children.add(Directory(name))
        elif line[0].isdigit():
            size, name = line.split(' ')
            name = name.strip()
            size = int(size)
            parent = current_path[-1]
            parent.children.add(File(name, size))
    return root


def sum_dir(directory, total):
    dir_sum = 0
    child_sum = 0
    for child in directory.children:
        if isinstance(child, Directory):
            child_sum += sum_dir(child, total)
        elif isinstance(child, File):
            dir_sum += child.size
    if dir_sum + child_sum < 100000:
        total[0] += dir_sum + child_sum
    return dir_sum + child_sum


def closest_dir(directory, space_needed, smallest_deletion):
    total = 0
    for child in directory.children:
        if isinstance(child, Directory):
            total += closest_dir(child, space_needed, smallest_deletion)
        elif isinstance(child, File):
            total += child.size
    if total >= space_needed:
        if total < smallest_deletion[0]:
            smallest_deletion[0] = total
    return total


def part1(commands):
    root = build_dir_tree(commands)
    total = [0]
    sum_dir(root, total)
    return total[0]


def part2(commands):
    root = build_dir_tree(commands)
    root_size = sum_dir(root, [0])
    space_used = 70000000 - root_size
    space_needed = 30000000 - space_used
    smallest_deletion = [maxsize]
    closest_dir(root, space_needed, smallest_deletion)
    return smallest_deletion[0]


test_input = read_input("Day07_test")
assert 95437 == part1(test_input)

real_input = read_input('Day07')
print(part1(real_input))

assert 24933642 == part2(test_input)
print(part2(real_input))

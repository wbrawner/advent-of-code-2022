#!/usr/bin/env python3

from pprint import pprint
from util import read_input


def part1(lines):
    visible = (len(lines) * 2) + (len(lines[0].strip()) * 2) - 4
    height = len(lines)
    width = len(lines[0])
    for i in range(0, height):
        for j in range(0, width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                continue
            tree = int(lines[i][j])
            visibleFromLeft = True
            for k in range(j - 1, -1, -1):
                other = int(lines[i][k])
                if other >= tree:
                    visibleFromLeft = False
                    break
            if visibleFromLeft:
                visible += 1
                continue
            visibleFromRight = True
            for k in range(j + 1, width):
                other = int(lines[i][k])
                if other >= tree:
                    visibleFromRight = False
                    break
            if visibleFromRight:
                visible += 1
                continue
            visibleFromTop = True
            for k in range(i - 1, -1, -1):
                other = int(lines[k][j])
                if other >= tree:
                    visibleFromTop = False
                    break
            if visibleFromTop:
                visible += 1
                continue
            visibleFromBottom = True
            for k in range(i + 1, height):
                other = int(lines[k][j])
                if other >= tree:
                    visibleFromBottom = False
                    break
            if visibleFromBottom:
                visible += 1
                continue
    return visible


def part2(lines):
    max_score = 0
    height = len(lines)
    width = len(lines[0])
    for i in range(0, height):
        for j in range(0, width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                continue
            tree = int(lines[i][j])
            leftScore = 0
            for k in range(j - 1, -1, -1):
                other = int(lines[i][k])
                leftScore += 1
                if other >= tree:
                    break
            rightScore = 0
            for k in range(j + 1, width):
                other = int(lines[i][k])
                rightScore += 1
                if other >= tree:
                    break
            topScore = 0
            for k in range(i - 1, -1, -1):
                other = int(lines[k][j])
                topScore += 1
                if other >= tree:
                    break
            bottomScore = 0
            for k in range(i + 1, height):
                other = int(lines[k][j])
                bottomScore += 1
                if other >= tree:
                    break
            total = leftScore * rightScore * topScore * bottomScore
            if total > max_score:
                max_score = total
    print('max: ' + str(max_score))
    return max_score


test_input = read_input("Day08_test")
assert 21 == part1(test_input)
real_input = read_input('Day08')
print(part1(real_input))
assert 8 == part2(test_input)
print(part2(real_input))

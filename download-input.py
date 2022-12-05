#!/usr/bin/python3

import argparse
import os
from os.path import exists
import shutil
from urllib.request import Request, urlopen
import webbrowser


def write_kotlin(day):
    with open(src_file, 'w') as src:
        src.write("""fun main() {{
    fun part1(input: List<String>): Int {{
        return 0
    }}

    fun part2(input: List<String>): Int {{
        return 0
    }}

    val testInput = readInput("Day{day}_test")
    check(part1(testInput) == 0)
    check(part2(testInput) == 0)

    val input = readInput("Day{day}")
    println(part1(input))
    println(part2(input))
}}""".format(day=day))


session_cookie = os.getenv('AOC_SESSION')
if not session_cookie:
    print('AOC_SESSION environment variable not set, aborting')
    exit(1)

if not session_cookie.startswith('session='):
    session_cookie = 'session=' + session_cookie

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--day', type=int)
args = parser.parse_args()

challenge_url = "https://adventofcode.com/2022/day/{}".format(args.day)
input_url = "{}/input".format(challenge_url)

webbrowser.open(challenge_url)

day_file_base = 'Day{}'.format(str(args.day).zfill(2))
day_file_test = 'kotlin/src/{}_test.txt'.format(day_file_base)

with open(day_file_test, 'w'):
    pass

request = Request(input_url, headers={'Cookie': session_cookie})
with urlopen(request) as response:
    with open('kotlin/src/{}.txt'.format(day_file_base), 'wb') as input_file:
        shutil.copyfileobj(response, input_file)

src_file = 'kotlin/src/{}.kt'.format(day_file_base)
if exists(src_file):
    exit(0)
write_kotlin(str(args.day).zfill(2))

#!/usr/bin/python3

from abc import ABC, abstractmethod
import argparse
from os import getenv
from os.path import exists, join
import shutil
from tempfile import TemporaryFile
from urllib.request import Request, urlopen
import webbrowser


class Language(ABC):
    src_path: str
    extension: str

    @abstractmethod
    def format_src(self, day):
        pass


class Kotlin(Language):
    src_path = 'kotlin/src'
    extension = 'kt'

    def format_src(self, day):
        return """fun main() {{
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
}}
""".format(day=day)


session_cookie = getenv('AOC_SESSION')
if not session_cookie:
    print('AOC_SESSION environment variable not set, aborting')
    exit(1)

if not session_cookie.startswith('session='):
    session_cookie = 'session=' + session_cookie

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--day', type=int, required=True)
parser.add_argument('--kotlin', action='store_true')
args = parser.parse_args()

challenge_url = "https://adventofcode.com/2022/day/{}".format(args.day)
input_url = "{}/input".format(challenge_url)

webbrowser.open(challenge_url)

languages = []

if args.kotlin:
    languages.append(Kotlin())

if len(languages) == 0:
    print("error: at least one language is required")
    parser.print_usage()
    exit(1)

day_file_base = 'Day{}'.format(str(args.day).zfill(2))
day_file_test = '{}_test.txt'.format(day_file_base)

request = Request(input_url, headers={'Cookie': session_cookie})
tmp_file = TemporaryFile()
with urlopen(request) as response:
    shutil.copyfileobj(response, tmp_file)

for language in languages:
    with open(join(language.src_path, day_file_test), 'w'):
        pass

    with open(join(language.src_path, '{}.txt'.format(day_file_base)), 'wb') as input_file:
        shutil.copyfileobj(tmp_file, input_file)

    src_file = join(language.src_path, '{}.{}'.format(day_file_base, language.extension))
    if not exists(src_file):
        with open(src_file, 'w') as src:
            src.write(language.format_src(str(args.day).zfill(2)))

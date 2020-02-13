#!/usr/bin python3
import argparse
from gendiff.engine import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='first file to compare')
    parser.add_argument('second_file', help='second file to compare')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == '__main__':
    main()

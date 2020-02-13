import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', help='first file to compare')
parser.add_argument('second_file', help='second file to compare')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()


def main():
    print('first_file - {}'.format(args.first_file))
    print('second_file - {}'.format(args.second_file))


if __name__ == '__main__':
    main()

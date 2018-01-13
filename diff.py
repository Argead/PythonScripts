#!/usr/bin/python3


def compare(file1, file2, mode='diff'):
    results = []
    with open(file1, 'r') as filea, open(file2, 'r') as fileb:
        for (index, (linea, lineb)) in enumerate(zip(filea, fileb)):
            if mode == 'diff':
                if linea != lineb:
                    results.append((index, linea, lineb))
            elif mode == 'same':
                if linea == lineb:
                    results.append((index, linea, lineb))
    return results


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file1', type=str)
    parser.add_argument('file2', type=str)
    parser.add_argument('mode', choices=['diff', 'same'], type=str, help='look for lines that are different, or the same in the two files')
    parser.add_argument('-s','--summary', action='store_true', help='only print the line numbers that are different between the two files')
    parser.add_argument('-r', '--remove-tabs', dest='remove', action='store_true', help='remove any whitespace at the ends of each line')
    args = parser.parse_args()
    result = compare(args.file1, args.file2, args.mode)
    
    for line in result:
        print(line[0])
        if not args.summary:
            if args.remove:
                stripped_line_one = line[1].strip()
                stripped_line_two = line[2].strip()
                print(stripped_line_one)
                print(stripped_line_two)
            else:
                print(line[1])
                print(line[2])
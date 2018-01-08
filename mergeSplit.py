#!/usr/bin/python3
"""
CLI utility to split or join files.
"""
import os
import sys

def merge_files(newFile, directory, readSize):
    with open(newFile, 'wb') as new_file_handle:
        pieces = os.listdir(directory)
        pieces.sort()
        for piece in pieces:
            path = os.path.join(directory, piece)
            with open(path, 'rb') as file_handle:
                while True:
                    bytes = file_handle.read(readSize)
                    if not bytes:
                        break
                    new_file_handle.write(bytes)


#TODO: implement glob
#TODO: implement try/except in both functions

def split_file(target, directory, readSize):
    if not os.path.exists(directory):
        os.mkdir(directory)
    for item in os.listdir(directory):
        os.remove(os.path.join(directory, item))
    count = 0
    with open(target, 'rb') as target_file:
        while True:
            piece = target_file.read(readSize)
            if not piece:
                break
            count += 1
            new_file_name = 'part{}'.format(count)
            new_file = os.path.join(directory, new_file_name)
            new_file_handle = open(new_file, 'wb')
            new_file_handle.write(piece)
            new_file_handle.close()
    return count
    
    
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['merge', 'split'], type=str, help='choose whether to split a file into pieces, or to merge those pieces back into a single file')
    parser.add_argument('target', type=str, help='for split mode, the target file to be split; for merge mode, the file to be created; provide an absolute file path or the script will use CWD')
    parser.add_argument('directory', type=str, help='for split mode, directory where the split pieces are go to; for merge mode, the directory containing the pieces to be merged')
    parser.add_argument('size', type=int, help='size of each piece of file to either be split or merged; should be a multiple of 2')
    args = parser.parse_args()
    
    if args.mode == 'merge':
        merge_files(args.target, args.directory, args.size)
    elif args.mode == 'split':
        split_file(args.target, args.directory, args.size)
    
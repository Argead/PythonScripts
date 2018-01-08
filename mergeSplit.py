#!/usr/bin/python3
"""
CLI utility to split or join files.
"""
import os
import sys


def merge_files(directory, newFile, readSize):
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

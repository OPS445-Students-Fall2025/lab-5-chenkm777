#!/usr/bin/env python3
# Author ID: kchen129

def read_file_string(file_name):
    """Return the entire contents of file_name as a single string."""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """
    Return the file contents as a list of lines WITHOUT newline characters.
    """
    with open(file_name, 'r') as f:
        return f.read().splitlines()

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

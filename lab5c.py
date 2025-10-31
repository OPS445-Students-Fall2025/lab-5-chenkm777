#!/usr/bin/env python3
# Author ID: kchen129

def add(number1, number2):
    """
    Add two numbers together.
    Accepts ints or numeric strings like '10'.
    On any error, return the exact string: 'error: could not add numbers'
    """
    try:
        n1 = int(str(number1).strip())
        n2 = int(str(number2).strip())
        return n1 + n2
    except Exception:
        return 'error: could not add numbers'

def read_file(filename):
    """
    Read a file and return a list of all lines INCLUDING newline characters.
    On any error, return the exact string: 'error: could not read file'
    """
    try:
        with open(filename, 'r') as f:
            return f.readlines()  # preserves '\n' like the sample output
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception

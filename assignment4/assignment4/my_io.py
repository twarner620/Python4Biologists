#!/usr/bin/env python3
# my_io.py

"""
This module exists to call the get_fh function, which will
open a file as a file handle with the specified method
"""


def get_fh(file, method):
    '''
    This function opens a file for reading or writing
    :param file: the file that is being opened
    :param method: reading or writing
    :return: a file hand in the specified mode: fh_in or fh_out
    :raises: IOError if file cannot be opened
    '''
    try:
        open(file, method)
        if method == 'r':
            fh_in = open(file, 'r')
            return fh_in
        if method == 'w':
            fh_out = open(file, 'w')
            return fh_out
        return None
    except ValueError:
        raise ValueError(f"{method} is not a valid opening method")
    except IOError:
        raise IOError(f"{file} cannot be opened")

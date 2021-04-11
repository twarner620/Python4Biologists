#!/usr/bin/env python3
# my_io.py

"""
This module exists to call the get_fh function, which will
open a file as a file handle with the specified method
"""

import os
from assignment5 import config

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"


def get_fh(file=None, method=None):
    '''
    This function opens a file for reading or writing
    :param file: the file that is being opened
    :param method: reading or writing
    :return: a file hand in the specified mode: fh_in or fh_out
    :raises: IOError if file cannot be opened
    '''
    try:
        fobj = open(file, method)
        return fobj
    except IOError as err:
        config.get_error_string_4_IOError(file, method)
        raise err
    except ValueError as err:
        config.get_error_string_4_ValueError()
        raise err
    except TypeError as err:
        config.get_error_string_4_TypeError()
        raise err


def is_valid_gene_file_name(file):
    '''
    This function returns True or false depending on if the specified
    file name exists
    :param file: the absolute path of unigene file
    :return: True/False if file exists
    '''
    return os.path.exists(file)

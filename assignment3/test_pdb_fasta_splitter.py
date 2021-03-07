#!/usr/bin/env python3
# test_pdb_fasta_splitter.py

'''
This script generates various tests for
pdb_fasta_splitter.py using pytest.
'''

import pytest
from pdb_fasta_splitter import get_fh, _check_size

ALPHABET = 'WXYZ'
DNA = 'ACTG'


def test_get_fh_4_ioerr():
    '''
    This test evaluates whether or not get_fh will raise an
    IOError if the provided file cannot be opened or does not
    exist
    :return: IOError
    '''
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_4_valerr():
    '''
    This test evaluates whether or not get_fh will raise an
    ValueError if the provided open method is not valid
    :return: ValueError
    '''
    with pytest.raises(ValueError):
        get_fh('ss.txt', 'qq')


def test__check_size():
    '''
    This test evaluates whether or not _check_size can
    accurately determine if two lists are the same length
    :return: None
    '''
    _check_size(ALPHABET, DNA)
    assert len(ALPHABET) == len(DNA)

#!/usr/bin/env python3
# test_nucleotide_statistics_from_fasta.py

'''
This script generates various tests for
nucloeitde_statistics_from_fasta.py using pytest.
'''

import pytest
from nucleotide_statistics_from_fasta import get_fh, _check_size, \
    _get_nt_occurence

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


def test__get_nt_occurence():
    '''
    This test evaluates whether or not _get_nt_occurence
    can accurately determine the number of nucleotides in
    a string sequence.
    :return: None
    '''
    num_a = _get_nt_occurence('A', DNA)
    assert num_a == 1


def test__get_nt_occurence_4_sysexit():
    '''
    This test evaluates whether or not _get_nt_occurence
    will raise a SystemExit if a string value other than
    A, C, T, G, or N is called.
    :return: SystemExit
    '''
    with pytest.raises(SystemExit):
        _get_nt_occurence('W', ALPHABET)

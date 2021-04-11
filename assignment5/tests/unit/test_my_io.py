#!/usr/bin/env python3
# test_my_io.py

"""
Test suite for my_io.py
"""

import os
import pytest
from assignment5 import my_io, config

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name does not conform to snake_case naming style"
# pylint: disable=C0103

FILE_2_TEST = "test.txt"
HORSE = "Equus_caballus"
HUMAN = "Homo_sapiens"
GENE = "API5"


def test_get_fh_4_IOError():
    with pytest.raises(IOError):
        my_io.get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    with pytest.raises(ValueError):
        my_io.get_fh(FILE_2_TEST, "qq")


def test_existing_get_fh_4_reading():
    _create_test_file(FILE_2_TEST)
    test = my_io.get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_writing():
    test = my_io.get_fh(FILE_2_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)


def test_is_valid_gene_file_name():
    file = "/".join((config.get_unigene_directory(), HORSE, GENE +
                     "." + config.get_unigene_extension()))
    assert my_io.is_valid_gene_file_name(file) is True, "File exists"


def _create_test_file(file):
    open(file, "w").close()

#!/usr/bin/env python3
# test_my_io.py

"""
Test suite for config.py
"""

import os
from assignment5 import config

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name does not conform to snake_case naming style"
# pylint: disable=C0103

HORSE = "Equus_caballus"
HUMAN = "Homo_sapiens"
GENE = "API5"
HOST_DICT = config.get_host_keywords()


def test_host_dict():
    assert HOST_DICT["horse"] == HORSE, "Correct host identified"
    assert HOST_DICT["humans"] == HUMAN, "Correct host identified"


def test_file_name_exists():
    file = "/".join((config.get_unigene_directory(), HORSE, GENE +
                     "." + config.get_unigene_extension()))
    assert os.path.exists(file) is True, "File found"

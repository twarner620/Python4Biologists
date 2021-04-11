#!/usr/bin/env python3
# config.py

'''
This module is used for configuration: obtaining file directory paths
and generating data structures.
'''

# Error" doesn't conform to snake_case naming style
# pylint: disable=invalid-name

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def get_error_string_4_IOError(file=None, mode=None):
    '''
    Prints an invalid argument statement and exits the program
    :param file: the specifie file name
    :param mode: the method to open the file
    :return: prints an invalid argument statement and sys.exits
    '''
    print(f"Could not open the file: {file} for mode '{mode}'")


def get_error_string_4_ValueError():
    '''
    Prints an invalid argument statement and exits the program
    '''
    print("Invalid argument Value for opening a file for reading/writing")


def get_error_string_4_TypeError():
    '''
    Prints an invalid argument statement and exits the program
    '''
    print("Invalid argument Type passed in:")


def get_unigene_directory():
    '''
    Returns the absolute path of the unigene directory
    '''
    return _UNIGENE_DIR


def get_unigene_extension():
    '''
    Returns the universal unigene file extension
    '''
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    '''
    Generates a dictionary to sanitize user input to assign
    the proper host keyword
    :return: a dictionary of host keywords
    '''
    bos_tarus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovies_aries"
    rattus_norvegicus = "Rattus_norvegicus"
    host_keywords = {
        "bos_taurus": bos_tarus,
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "homo_sapiens": homo_sapiens,
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "equus_caballus": equus_caballus,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "mus_musculus": mus_musculus,
        "mus musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,
        "ovis_aries": ovis_aries,
        "ovis aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus_norvegicus": rattus_norvegicus,
        "rattus norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus
    }
    return host_keywords

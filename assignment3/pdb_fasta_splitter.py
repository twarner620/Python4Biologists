#!/usr/bin/env python3
# pdb_fasta_splitter.py

'''
This program defines a function that opens a given file for reading that
contains both sequence and secondary structure data. The sequence data and
secondary structure data are split into two output files, pdb_protein.fasta
and pdb_ss.fasta, respectively.
'''

import re
import argparse
import sys


def main():
    '''
    This is the main function of the script, which calls various ancillary
    functions to open a file, split the data into lists, split the data and
    write it to two separate fasta files.
    :return: pdb_protein.fasta and pdb_ss.fasta
    '''
    args = get_cli_args()
    file = args.infile
    fh_in = get_fh(file, 'r')
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_in.close()
    fh_out1 = get_fh("pdb_protein.fasta", 'w')
    fh_out2 = get_fh("pdb_ss.fasta", 'w')
    split_lists(list_headers, list_seqs, fh_out1, fh_out2)
    fh_out1.close()
    fh_out2.close()


def get_cli_args():
    '''
    This function obtains the user-provided arguments from the command
    line as well as providing a help function.
    :return: infile
    '''
    parser = argparse.ArgumentParser(
        description='Give the fasta sequence file '
                    'name to do the splitting')
    parser.add_argument('-i', '--infile',
                        dest='infile',
                        type=str,
                        help='Path to the file to open',
                        required=True)
    return parser.parse_args()


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


def get_header_and_sequence_lists(handle):
    '''
    This function iterates through the input file and splits the
    data into two lists. It also calls _check_list_size to make sure
    the fasta file is formatted properly
    :param handle: the file being processed, fh_in
    :return: list_headers and list_seqs
    '''
    list_headers = []
    list_seqs = []
    okazaki = []
    for line in handle:
        line = line.rstrip()
        if re.match('^>', line):
            list_headers.append(line)
            if okazaki:
                okazaki = "".join(okazaki)
                list_seqs.append(okazaki)
                okazaki = []
        else:
            okazaki.append(line)
    if okazaki:
        okazaki = "".join(okazaki)
        list_seqs.append(okazaki)
    _check_size(list_headers, list_seqs)
    return list_headers, list_seqs


def _check_size(list_headers, list_seqs):
    '''
    This sub-function ensures that list_headers and list_seqs
    are the same length
    :param list_headers: the list of headers from get_header_and_sequence_lists
    :param list_seqs: the list of sequences from get_header_and_sequence_lists
    :return: Prints the number of protein and secondary
    structure sequences found
    '''
    h_size = len(list_headers)
    s_size = len(list_seqs)
    seq_counts = s_size / 2
    seq_counts = int(seq_counts)
    if h_size == s_size:
        print(f"Found {seq_counts} protein sequences\n"
              f"Found {seq_counts} ss sequences")
    else:
        sys.exit("The size of the sequence and the header"
                 "lists is different\nAre you sure the FASTA"
                 "is in correct format")


def split_lists(list_headers, list_seqs, fh_out1, fh_out2):
    '''
    This function takes the two lists from get_header_and_sequence_lists and
    writes the data to two separate fasta files.
    :param list_headers: the list of headers from get_header_and_sequence_lists
    :param list_seqs: the list of sequences from get_header_and_sequence_lists
    :param fh_out1: file hand for pdb_protein.fasta
    :param fh_out2: file hand for pdb_ss.fasta
    :return: Two separate fasta files containing the amino acid sequences and
    secondary structure data from the original file
    '''
    for i, header in enumerate(list_headers):
        if re.search('sequence$', header):
            fh_out1.write(">{}\n{}\n".format(header, list_seqs[i]))
        if re.search('secstr$', header):
            fh_out2.write(">{}\n{}\n".format(header, list_seqs[i]))


if __name__ == "__main__":
    main()

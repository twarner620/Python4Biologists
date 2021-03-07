#!/usr/bin/env python3
# nucleotide_statistics_from_fasta.py

'''
This program iterates through a fasta file, counting the number
of nucleotides in each sequence and calculates the GC% content.
The nucleotide statistics as well as the accession ID of each
sequence are written to a tab separated file.
'''

import argparse
import re
import sys


def main():
    '''
    This function calls all the other primary functions in this
    program. It obtains the user-provided input from the command
    line, opens the input file for reading, iterates through it,
    storing the header and sequence data into separate lists. It
    then calculates statistics of each sequence and prints the
    stats as well as the accession ID for each sequence to a
    tab separated file named as the output file name specified by
    the user
    :return: tab separated statistics file
    '''
    args = get_cli_args()
    fh_in = get_fh(args.infile, 'r')
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_in.close()
    fh_out = get_fh(args.outfile, 'w')
    print_sequence_stats(list_headers, list_seqs, fh_out)
    fh_out.close()


def get_cli_args():
    '''
    This function obtains the user-provided arguments from the command
    line as well as providing a help function.
    :return: infile and outfile
    '''
    parser = argparse.ArgumentParser(
        description='Give the fasta sequence file name'
                    ' to get the nucleotide statistics')
    parser.add_argument('-i', '--infile',
                        dest='infile',
                        type=str,
                        help='Path to the file to open',
                        required=True)
    parser.add_argument('-o', '--outfile',
                        dest='outfile',
                        type=str,
                        help='Path to the file to write',
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
    ;:return A system exit error if the list sizes are not equal
    '''
    h_size = len(list_headers)
    s_size = len(list_seqs)
    if h_size != s_size:
        sys.exit("The size of the sequence and the header"
                 "lists is different\nAre you sure the FASTA"
                 "is in correct format")


def print_sequence_stats(list_headers, list_seqs, fh_out):
    '''
    This function calculates the number of each nucleotide present
    and the accession ID of each sequence by calling _get_nt_occurrence
    and _get_accession, respectively. With this data, the GC% of the sequence
    is calculated and then all the data is written to a tab separated file
    :param list_headers: the list of headers from get_header_and_sequence_lists
    :param list_seqs: the list of sequences from get_header_and_sequence_lists
    :param fh_out: the user-defined output file name as a handle
    :return: A tab separated file containing nucleotide statistics for each
    sequence in the fasta file provided
    '''
    for i, seq in enumerate(list_seqs,):
        fh_out.write("Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%")
        count = i + 1
        header_string = list_headers[i]
        accession_string = _get_accession(header_string)
        num_a = _get_nt_occurence('A', seq)
        num_c = _get_nt_occurence('C', seq)
        num_g = _get_nt_occurence('G', seq)
        num_t = _get_nt_occurence('T', seq)
        num_n = _get_nt_occurence('N', seq)
        seq_length = num_a + num_c + num_g + num_t + num_n
        gc_ratio = ((num_g + num_c) / seq_length) * 100
        fh_out.write(f"\n{count}\t{accession_string}\t{num_a}"
                     f"\t{num_g}\t{num_c}\t{num_t}\t{num_n}\t"
                     f"{seq_length}\t{gc_ratio:.1f}\n")


def _get_accession(header_string):
    '''
    This sub-function splits the header string of the fasta file and
    returns the accession number.
    :param header_string: the iteration of header from
    get_header_and_sequence_lists
    :return: the accession number of the header
    '''
    header_parts = header_string.split()
    accession_num = header_parts[0]
    accession_num = accession_num[1:]
    return accession_num


def _get_nt_occurence(nucleotide, sequence):
    '''
    This sub-function counts the number of nucleotides present
    in a sequence string. If a character other than A, C, T, G, or
    N is called, the program will raise a system exit
    :param nucleotide: A, C, T, G, or N as a string
    :param sequence: the iteration of sequence data from
    get_header_and_sequence_lists
    :return: the number of the specified nucleotide in the sequence
    '''
    if nucleotide in ('A', 'C', 'T', 'G', 'N'):
        return sequence.count(nucleotide)
    sys.exit("Did not code this condition")


if __name__ == "__main__":
    main()

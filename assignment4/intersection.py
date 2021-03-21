#!/usr/bin/env python3
# intersection.py

'''
This program takes two files from the user, each containing various
gene names. The program then compares the two files, returning only
the genes found in common to a text file.
'''

import argparse
import os
from assignment4 import my_io


def main():
    """
    This is the main function of the program, which calls various
    other functions to iterate through two user-provided files which
    contain gene names and returns the number of unique genes found
    in each file as well as the number of common genes to STDOUT. The
    list of common genes is also written to a text file.
    :return: a text file containing the common genes
    """
    args = get_cli_args()
    file_1, file_2 = args.infile1, args.infile2
    handle1 = my_io.get_fh(file_1, 'r')
    handle2 = my_io.get_fh(file_2, 'r')
    gene_list_1 = get_gene_symbs(handle1)
    gene_list_2 = get_gene_symbs(handle2)
    handle1.close()
    handle2.close()
    out_dir = "OUTPUT/"
    os.makedirs(out_dir, exist_ok=True)
    handle_out = my_io.get_fh(out_dir + 'intersection.txt', 'w')
    print_data(handle_out, gene_list_1, gene_list_2, file_1, file_2)


def get_cli_args():
    '''
    This function obtains the user-provided arguments from the command
    line as well as providing a help function.
    :return: infile1 first list of gene names
    :return: infile2 second list of gene names
    '''
    parser = argparse.ArgumentParser(
        description='Provide two gene list (ignore header line), '
                    'find intersection')
    parser.add_argument('-i1', '--infile1',
                        dest='infile1',
                        type=str,
                        help='Gene list 1 to open',
                        default="chr21_genes.txt")
    parser.add_argument('-i2', '--infile2',
                        type=str,
                        help='Gene list 2 to open',
                        dest='infile2',
                        default="HUGO_genes.txt")
    return parser.parse_args()


def get_gene_symbs(handle):
    """
    This function iterates through the gene list file, storing
    each gene name into a list before converting to a set.
    :param handle: a gene list as a file handle
    :return: a set of gene symbols
    """
    g_symbs = []
    handle.readline()
    for line in handle:
        line = line.split("\t")
        g_symbs.append(line[0])
    return set(g_symbs)


def print_data(handle_out, gene_list_1, gene_list_2, infile1, infile2,):
    """
    This function compiles all the data generated in this program, printing
    a summary to STDOUT and returning all common gene names to a designated
    output text file.
    :param handle_out: the output file handle
    :param gene_list_1: the first set of gene names
    :param gene_list_2: the second set of gene names
    :param infile1: the first gene list file name
    :param infile2: the second gene list file name
    :return: The unique and common gene names retured to
    STDOUT and the intersection of the two written to the
    output file.
    """
    common_genes = gene_list_1.intersection(gene_list_2)
    print(f"Number of unique gene names in {infile1}: {len(gene_list_1)}")
    print(f"Number of unique gene names in {infile2}: {len(gene_list_2)}")
    print(f"Number of common gene symbols found: {len(common_genes)}")
    for i in common_genes:
        handle_out.write(i + "\n")
    print(f"Output stored in OUTPUT/intersection.txt")
    handle_out.close()


if __name__ == "__main__":
    main()

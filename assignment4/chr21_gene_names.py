#!/usr/bin/env python3
# chr21_gene_names.py

"""
This script generates a dictionary of gene names and descriptions based
on user-provided input. The generated dictionary is then queried by the
user to search for the gene description when provided the gene name.
"""

import argparse
import sys
from assignment4 import my_io


def main():
    """
    This is the main function of this program, which calls various
    functions to obtain the file from the user at the command line,
    generates a dictionary of the genes and their descriptions, and
    then interacts with the user to query the dictionary.
    :return: Gene description printed to STDOUT
    """
    args = get_cli_args()
    infile = args.infile
    handle = my_io.get_fh(infile, 'r')
    gene_dict = generate_dict(handle)
    get_user_input(gene_dict)
    infile.close()


def get_cli_args():
    '''
    This function obtains the user-provided arguments from the command
    line as well as providing a help function.
    :return: infile
    '''
    parser = argparse.ArgumentParser(
        description='Open chr21_genes.txt, and ask user for a gene name')
    parser.add_argument('-i', '--infile',
                        dest='infile',
                        type=str,
                        help='Path to the file to open',
                        required=True)
    return parser.parse_args()


def generate_dict(handle):
    """
    This function generates a dictionary of the gene symbols and
    their descriptions.
    :param handle: the file handle containing the gene data
    :return: a dictionary of gene symbols and their descriptions
    """
    g_sym = []
    g_desc = []
    for line in handle:
        line = line.rstrip().split("\t")
        g_sym.append(line[0])
        g_desc.append(line[1])
    return dict(zip(g_sym, g_desc))


def get_user_input(gene_dict):
    """
    This function interacts with the user at the command line to
    query the dictionary.
    :param gene_dict: The dictionary of gene names and descriptions
    created by generate_dict()
    :return: Gene description printed to STDOUT
    """
    gene = input("Enter gene name of interest. Type quit to exit:\t")
    if gene.lower() == 'quit':
        sys.exit("Thanks for querying the data")
    try:
        description = gene_dict[gene]
        print(f"{gene} found! Here is the description:\n{description}")
    except KeyError:
        print("Not a valid gene name.")


if __name__ == "__main__":
    main()

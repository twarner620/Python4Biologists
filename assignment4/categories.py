#!/usr/bin/env python3
# categories.py

'''
This script takes two files, provided by the user from the command
line, which containing gene names, categories, and occurrence of those
categories. These data are converted to dictionaries to calculate the
relative abundance of each gene category and the results are then
printed to a tab separated file.
'''

import argparse
import os
from assignment4 import my_io


def main():
    """
    This is the main function of this program, which calls various
    functions to iterate through tab separated files of gene names,
    categories, and descriptions to generate dictionaries and compile
    the data into a tab separated file with relative occurrences.
    :return: a  tab separated file containing the gene categories,
    their relative occurrences, and the descriptions of the categories
    """
    args = get_cli_args()
    file_1, file_2 = args.infile1, args.infile2
    handle1 = my_io.get_fh(file_1, 'r')
    handle2 = my_io.get_fh(file_2, 'r')
    gene_dict = generate_dict(handle2)
    counts = count_ocurrences(handle1)
    handle1.close()
    handle2.close()
    out_dir = "OUTPUT/"
    os.makedirs(out_dir, exist_ok=True)
    handle_out = my_io.get_fh(out_dir + 'categories.txt', 'w')
    print_data(handle_out, gene_dict, counts)


def get_cli_args():
    '''
    This function obtains the user-provided arguments from the command
    line as well as providing a help function.
    :return: infile1 the name of the file containing genes and their categories
    :return: infile2 the name of the file containing gene categories and their
    descriptions
    '''
    parser = argparse.ArgumentParser(
        description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1', '--infile1',
                        dest='infile1',
                        type=str,
                        help='Path to the gene description file to open',
                        default="chr21_genes.txt")
    parser.add_argument('-i2', '--infile2',
                        dest='infile2',
                        type=str,
                        help='Path to the gene category to open',
                        default="chr21_genes_categories.txt")
    return parser.parse_args()


def generate_dict(handle):
    """
    This function generates a dictionary of the category symbols and
    their descriptions.
    :param handle: the file handle containing the gene category data
    :return: a dictionary of gene category symbols and their descriptions
    """
    cat_symb = []
    cat_desc = []
    for line in handle:
        line = line.rstrip().split("\t")
        cat_symb.append(line[0])
        cat_desc.append(line[1])
    return dict(zip(cat_symb, cat_desc))


def count_ocurrences(handle):
    """
    This function returns a dictionary containing the number of
    occurrences of each gene category
    :param handle: the file handle of all the genes
    :return: a dictionary of gene category counts
    """
    categories = []
    handle.readline()
    for line in handle:
        line = line.rstrip().split("\t")
        try:
            categories.append(line[2])
        except IndexError:
            pass
    counts = dict()
    for i in categories:
        counts[i] = counts.get(i, 0) + 1
    counts = dict(sorted(counts.items()))
    return counts


def print_data(handle_out, gene_dict, counts):
    """
    This function prints the data generated in this program to the
    output file
    :param handle_out: The file handle to write to
    :param gene_dict: the dictionary of genes created by generate_dict
    :param counts: the number of occurrences for each gene category
    :return: a tab separated file containing the gene categories,
    their relative occurrences, and the descriptions of the categories
    """
    handle_out.write("\tCategory\tOccurrence\tDescription")
    for (k_1, v_1), (k_2, v_2) in zip(gene_dict.items(), counts.items()):
        if k_1 == k_2:
            handle_out.write(f"\n{k_1}\t{v_2}\t{v_1}")
    handle_out.close()


if __name__ == "__main__":
    main()

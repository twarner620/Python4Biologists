# Assignment 4

## Author: Tyler Warner

Language(s) used:
- Python3

In this assignment, three programs were coded: ch21_gene_names.py, categories.py, and intersection.py. A module, my_io.py, that opens a file with a specified method, which was implemented each time a file had to be opened in the three programs. chr21_gene_names.py iterates through a tab separated list of genes found on human chromosome 21 and the gene descriptions, generating a dictionary of these key-value pairs. The user is then prompted to query the dictionary. categories.py via the command line. In categories.py, the relative abundances of the categories of genes on human chromosome 21 are calculated and entered into a dictionary. This data is then written to a tab separated file: OUTPUT/categories.txt. Finally, intersection.py calculates the number of unique genes found in two separate gene lists and the number of common genes. These common genes are written to a file: OUTPUT/intersection.py.

Additionally, a test suite for my_io.py was generated: /tests/unit/test_my_io.py 

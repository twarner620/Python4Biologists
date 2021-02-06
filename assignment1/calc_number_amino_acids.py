#!/usr/bin/env python3
# calc_number_amino_acids.py

import sys

GeneName = input("Please enter a gene name: ")
print("Your gene of interest is " + GeneName + "!")
GeneLength = input("Please indicate the length coding region of your gene: ")
DivisibleBy3 = int(GeneLength) % 3
if DivisibleBy3 != 0:
    sys.exit("You entered a gene length not divisible by 3. Please double check your ORF!")
print("You've indicated the length of {} is {} bp!".format(GeneName, GeneLength))
ProteinLength = int(GeneLength)/3
print("Once translated, {} will be {:.0f} amino acids long!".format(GeneName, ProteinLength))
ProteinWeight = (int(ProteinLength)*110)/1000
print("The average weight of the {} protein is {} kDa!".format(GeneName, ProteinWeight))

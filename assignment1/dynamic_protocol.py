#!/usr/bin/env python3
# dynamic_protocol.py

FinalVol = input("Please indicate the final volume of your solution in mL: ")
NaClStock = input("Please indicate the stock concentration of NaCl available in nM: ")
NaClFinal = input("Please indicate the desired final concentration of NaCl in nM: " )
MgCl2Stock = input("Please indicate the stock concentration of MgCl2 available in nM: ")
MgCl2Final = input("Please indicate the desired final concentration of MgCl2 in nM: ")

NaClDil = float(FinalVol) * (float(NaClFinal) / float(NaClStock))
MgCl2Dil = float(FinalVol) * (float(MgCl2Final) / float(MgCl2Stock))
QSVol = float(FinalVol) - (NaClDil + MgCl2Dil)


step1 = "Add " + str(NaClDil) + " mL NaCl.\n"
step2 = "Add " + str(MgCl2Dil) + " mL MgCl2.\n"
step3 = "Add " + str(QSVol) + " mL water and mix.\n"
print(step1+step2+step3)

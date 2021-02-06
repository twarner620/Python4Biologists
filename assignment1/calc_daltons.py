#!/usr/bin/env python3
# calc_daltons.py

protein_sequence = " madpaagppp segeestvrf arkgalrqkn vhevknhkft arffkqptfc shctdfiwgf gkqgfqcqvc" \
                   " cfvvhkrche fvtfscpgad kgpasddprs khkfkihtys sptfcdhcgs llyglihqgm kcdtcmmnvh" \
                   " krcvmnvpsl cgtdhterrg riyiqahidr evlivvvrda knlvpmdpng lsdpyvklkl ipdpkseskq" \
                   " ktktikcsln pewnetfrfq lkesdkdrrl sveiwdwdlt srndfmgsls fgiselqkag vdgwfkllsq" \
                   " eegeyfnvpv ppegsegnee lrqkferaki gqgtkapeek tantiskfdn ngnrdrmklt dfnflmvlgk" \
                   " gsfgkvmlse rkgtdelyav kilkkdvviq dddvectmve krvlalpgkp pfltqlhscf qtmdrlyfvm" \
                   " eyvnggdlmy hiqqvgrfke phavfyaaei aiglfflqsk giiyrdlkld nvmldseghi kiadfgmcke" \
                   " niwdgvttkt fcgtpdyiap eiiayqpygk svdwwafgvl lyemlagqap fegededelf qsimehnvay" \
                   " pksmskeava ickglmtkhp gkrlgcgpeg erdikehaff ryidwekler keiqppykpk ardkrdtsnf" \
                   " dkeftrqpve ltptdklfim nldqnefagf sytnpefvin v"
# to get rid of newline characters
protein_sequence = protein_sequence.replace(" ", "")
protein_length = len(protein_sequence)
protein_weight = (protein_length*110)/1000
protein_name = "Protein kinase C beta type"
print("The length of \"{}\" is {} amino acids.\nThe average weight of "
      "this protein sequence is {} kDa".format(protein_name, protein_length, protein_weight))

"""Function which performs chi squared test on homogenity for dichotomous variables, 2 samples.

(To be updated so it works for variables with more gradation and higher number of samples.)
The result given is either 'not significant' or significant at a certain alpha level (10% / 5% / 1%).
Background to test: Used when comparing differences in distributions of 2+ samples with data on any scale of measure.
"""

import math

__author__ = 'Kriegerprinzessin'
__email__ = 'thesearemyrepos@gmail.com'

# test data
percs_S1_test = [76, 67, 83, 74, 68, 71, 73]
percs_S2_test = [65, 54, 75, 60, 56, 68, 62]
ns_S1_test = [98, 27, 78, 96, 96, 94, 96]
ns_S2_test = [150, 48, 126, 146, 149, 142, 149]

# percs_S1 = % of category A of different items/variables for sample 1 (e. g. current percentages)
# percs_S2 = % of category A of different items/variables for sample 2 (e. g. last percentages)
# ns_S1 = ns for items/variables for sample 1
# ns_S2 = ns for items/variables for sample 2
def chi_homogenity(percs_S1, percs_S2, ns_S1, ns_S2):

    # calculate all observed and expected cell values
    values_chi_calc = []
    for idx, perc in enumerate(percs_S1):
        values_chi_calc.append([]) # creates item sublist
        values_chi_calc[idx].append([]) # creates observed sublist in item sublist
        values_chi_calc[idx].append([]) # creates expected sublist in item sublist
        values_chi_calc[idx][0].append(float(perc/100*ns_S1[idx])) # nA 1
        values_chi_calc[idx][0].append(float(ns_S1[idx]-values_chi_calc[idx][0][-1])) # nB 1
        values_chi_calc[idx][0].append(float(percs_S2[idx]/100*ns_S2[idx])) # nA 2
        values_chi_calc[idx][0].append(float(ns_S2[idx]-values_chi_calc[idx][0][-1])) # nB 2
        values_chi_calc[idx][1].append(float(ns_S1[idx]*(values_chi_calc[idx][0][-4]+values_chi_calc[idx][0][-2])/(ns_S1[idx]+ns_S2[idx]))) # eA 1
        values_chi_calc[idx][1].append(float(ns_S1[idx]*(values_chi_calc[idx][0][-3]+values_chi_calc[idx][0][-1])/(ns_S1[idx]+ns_S2[idx]))) # eB 1
        values_chi_calc[idx][1].append(float(ns_S2[idx]*(values_chi_calc[idx][0][-4]+values_chi_calc[idx][0][-2])/(ns_S1[idx]+ns_S2[idx]))) # eA 2
        values_chi_calc[idx][1].append(float(ns_S2[idx]*(values_chi_calc[idx][0][-3]+values_chi_calc[idx][0][-1])/(ns_S1[idx]+ns_S2[idx]))) # eB 2

    print(values_chi_calc)

    # calculate degrees of freedom and test statistic
    dfs = (2-1)*(2-1) # i know it's silly atm
    x_2_list = []
    x_2 = 0
    for item in values_chi_calc:
        for cell in range(len(item[0])):
            x_2 += math.pow(item[0][cell]-item[1][cell], 2)/item[1][cell]
        x_2_list.append(x_2)
        x_2 = 0

    print(dfs, x_2_list)

    # chi squared critical values for different alpha levels and dfs for each
    p_10 = [2.71, 4.61, 6.25, 7.78, 9.24, 10.64, 12.02, 13.36, 14.68, 15.99]
    p_5 = [3.84, 5.99, 7.81, 9.49, 11.07, 12.59, 14.07, 15.51, 16.92, 18.31]
    p_1 = [6.63, 9.21, 11.34, 13.28, 15.09, 16.81, 18.48, 20.09, 21.67, 23.21]

    for idx, chi in enumerate(x_2_list):
        ########################## formatted string?
        if chi > p_1[dfs-1]:
            print("Item/Variable " + str(idx +1) + ": p < .01")
        elif chi > p_5[dfs-1]:
            print("Item/Variable " + str(idx +1) + ": p < .05")
        elif chi > p_10[dfs-1]:
            print("Item/Variable " + str(idx +1) + ": p < .10")
        else:
            print("Item/Variable " + str(idx +1) + ": n. s.")

chi_homogenity(percs_S1_test, percs_S2_test, ns_S1_test, ns_S2_test)



# for reference: list_chi_calc structure

#   ------ Item #1 ------- ------ Item #2 -------
#     ---obs--  ---exp--     ---obs--  ---exp--
# [ [[nAnBnAnB][eAeBeAeB]] [[nAnBnAnB][eAeBeAeB]] ]
#     -S1--S2-  -S1--S2-     -S1--S2-  -S1--S2-

# obs: observed exp: expected
# A: one level B: the other level
# S1: one sample S2: another sample

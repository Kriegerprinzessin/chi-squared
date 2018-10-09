"""Function which performs chi squared test on homogenity for dichotomous variables.

(To be updated so it works for variables with more gradation.)
The result given is either 'not significant' or significant at a certain alpha level (10% / 5% / 1%).
Background to test: Used when comparing differences in distributions of 2+ samples with data on any scale of measure.
"""

__author__ = 'Kriegerprinzessin'
__email__ = 'thesearemyrepos@gmail.com'



# for one dichotomous item/question, percs = % of different groups, ns = ns of different groups
def chi_homogenity(percs, ns):
	# calculate first column via % and n, second column via n - first	
	column_values_found = [[],[]]
	for idx, perc in enumerate(percs):
		column_values_found[0].append(float(perc/100*ns[idx]))
		column_values_found[1].append(float(ns[idx]-column_values_found[0][idx]))
	# calculate expected cell values
	column_values_expected = [[],[]]
	for idx, value in enumerate(column_values_found[0]):
		column_values_expected[0].append((column_values_found[0][idx]+column_values_found[1][idx])*sum(column_values_found[0])/(sum(column_values_found[0])+sum(column_values_found[1])))
	for idx, value in enumerate(column_values_found[1]):
		column_values_expected[1].append((column_values_found[0][idx]+column_values_found[1][idx])*sum(column_values_found[1])/(sum(column_values_found[0])+sum(column_values_found[1])))
	print(column_values_found)
	print(column_values_expected)
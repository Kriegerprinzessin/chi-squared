"""Function which performs chi squared test on homogenity for dichotomous variables.

(To be updated so it works for variables with more gradation.)
The result given is either 'not significant' or significant at a certain alpha level (10% / 5% / 1%).
Background to test: Used when comparing differences in distributions of 2+ samples with data on any scale of measure.
"""

__author__ = 'Kriegerprinzessin'
__email__ = 'thesearemyrepos@gmail.com'

# test data
percs_obs_test = [76, 67, 83, 74, 68, 71, 73]
percs_exp_test = [65, 54, 75, 60, 56, 68, 62]
ns_obs_test = [98, 27, 78, 96, 96, 94, 96]

## for one dichotomous item/question
# percs_obs = % of category 1 of different (sub)groups/items OBSERVED (e. g. current distribution)
# percs_exp = % of category 1 of different (sub)groups/items EXPECTED (e. g. last/typical distribution)
# ns_obs = ns for (sub)groups/items OBSERVED
def chi_homogenity(percs_obs, percs_exp, ns_obs):
    # calculate observed values: [category 1] via percs_obs and ns_obs, [category 2] via ns_obs - category 1
    values_found = [[],[]]
    for idx, perc in enumerate(percs_obs):
        values_found[0].append(float(perc/100*ns_obs[idx]))
        values_found[1].append(float(ns_obs[idx]-values_found[0][idx]))
    # calculate expected values: [category 1] via percs_exp and ns_obs, [category 2] via ns_obs - category 1
    values_expected = [[],[]]
    for idx, perc in enumerate(percs_exp):
        values_expected[0].append(float(perc/100*ns_obs[idx]))
        values_expected[1].append(float(ns_obs[idx]-values_expected[0][idx]))

    print(values_found)
    print(values_expected)

chi_homogenity(percs_obs_test, percs_exp_test, ns_obs_test)

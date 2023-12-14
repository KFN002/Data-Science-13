from scipy.stats import chi2_contingency
import numpy as np


def convert_to_float(x):
    return float(str(x).replace(',', '.'))


def cramers_v(crosstab):
    chi2 = chi2_contingency(crosstab)[0]
    return np.sqrt(chi2 / (crosstab.sum().sum() * (min(crosstab.shape) - 1)))


def correlation_ratio(categories, values):
    categories = np.array(categories)
    values = np.array(values)
    ssw = 0
    ssb = 0
    for category in set(categories):
        subgroup = values[np.where(categories == category)[0]]
        ssw += sum((subgroup - np.mean(subgroup)) ** 2)
        ssb += len(subgroup) * (np.mean(subgroup) - np.mean(values)) ** 2
    return (ssb / (ssb + ssw)) ** .5

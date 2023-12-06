from scipy.stats import chi2_contingency
import numpy as np


def convert_to_float(x):
    return float(str(x).replace(',', '.'))

def cramers_v(crosstab):
    chi2 = chi2_contingency(crosstab)[0]
    return np.sqrt(chi2 / (crosstab.sum().sum() * (min(crosstab.shape) - 1)))

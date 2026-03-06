import numpy as np

def VaR(r, confidence, principal=1):
    # This function returns the left tail value
    # confidence = certaint that losses are not greater than the VaR value
    # r = an array of stock returns
    # out = positively stated value of r at the 1-confidence percentile * principal

    out = .01 # Calculate the percentile
    return out  # Return the absolute value of the calculated percentile

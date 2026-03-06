import numpy as np

def es(losses, confidence=None, VaR=None, use_PnL=False):
    """
    Calculate the Expected Shortfall (ES) of losses.

    losses: array of positively stated loss values
    confidence: risk level (e.g., 0.99 for 99%)
    VaR: dollar value specifying the VaR threshold

    return Expected Shortfall as the average of losses exceeding VaR
    """

    losses = np.array(losses)

    if VaR is None:
        VaR = np.percentile(losses, 100 * confidence)

    es_value = np.mean(losses[losses > VaR])

    return es_value

u = np.random.uniform(0, 100, 100000)

es_confidence = es(losses=u, confidence=0.8)
print('ES with confidence:', np.round(es_confidence, 0) == 90)

es_var = es(losses=u, VaR=80)
print('ES with VaR:', np.round(es_var, 0) == 90)

import math
from config import config

class nrtl:
    def __init__(self, interactions):
        self.tau = interactions

    def activity_coefficients(self, x):
        g = {}
        theta = {}
        for key in config.components:
            theta[key] = math.exp(-self.tau[key])
        for i in config.components:
            sum_term = sum(x[j] * self.tau[(i,j)] for j in config.components)
            g[i] = math.exp(-self.tau[(i,i)] * (sum_term))
        return g

class wilson:
    def __init__(self, interactions):
        self.l = interactions

    def activity_coefficients(self, x):
        gamma = {}
        for i in config.components:
            sum_term = sum(x[j] * self.l[(i,j)] for j in config.components)
            gamma[i] = math.exp(-self.l[(i,i)] * (1 - x[i]) + sum_term)
        return gamma

class peng_robinson:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def equation_of_state(self, T, P):
        # simplistic implementation
        return (self.a / (T * (P + self.b)))

def get_model():
    if config.model == 'nrtl':
        return nrtl(config.binary_interactions)
    elif config.model == 'wilson':
        return wilson(config.binary_interactions)
    elif config.model == 'peng_robinson':
        a = sum([config.constants[i]['a'] for i in config.components])
        b = sum([config.constants[i]['b'] for i in config.components])
        return peng_robinson(a, b)
    else:
        raise ValueError("model not supported")

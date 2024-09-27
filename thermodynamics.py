from models import get_model
from config import config

def raoult_law(x, P, Psat):
    return x * Psat

def calculate_vle(T, P, Psat):
    model = get_model()
    gamma = model.activity_coefficients(x={comp: 1/len(config.components) for comp in config.components})
    y = raoult_law(x={comp:1/len(config.components) for comp in config.components}, P=P, Psat=Psat)
    return y

def fugacity_coefficients(T, P):
    model = get_model()
    return model.equation_of_state(T, P)

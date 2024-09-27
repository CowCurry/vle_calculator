import pandas as pd
from config import config

def load_component_data():
    df = pd.DataFrame(config.constants).transpose()
    df['binary_interaction'] = df.index.map(lambda x: config.binary_interactions.get(x, 0))
    return df

def generate_conditions():
    temperatures = list(range(config.temperature_range[0], config.temperature_range[1]+1, config.step_temperature))
    pressures = [round(p,2) for p in frange(config.pressure_range[0], config.pressure_range[1], config.step_pressure)]
    return temperatures, pressures

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

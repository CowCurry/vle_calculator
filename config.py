import os

class config:
    data_dir = os.path.join(os.getcwd(), 'data')
    results_dir = os.path.join(os.getcwd(), 'results')
    plots_dir = os.path.join(os.getcwd(), 'plots')
    components = ['water', 'ethanol']
    temperature_range = (280, 350)  # kelvin
    pressure_range = (0.1, 10)  # bara
    step_temperature = 5
    step_pressure = 0.5
    model = 'nrtl'  # options: 'nrtl', 'wilson', 'peng_robinson'
    constants = {
        'water': {'a': 0.0, 'b': 0.0},
        'ethanol': {'a': 1.0, 'b': 0.5}
    }
    binary_interactions = {
        ('water', 'ethanol'): 0.3,
        ('ethanol', 'water'): 0.3
    }
    tolerance = 1e-6
    max_iterations = 1000
    save_results = True
    verbose = True

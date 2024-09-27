import os
from config import config

def initialize_directories():
    os.makedirs(config.data_dir, exist_ok=True)
    os.makedirs(config.results_dir, exist_ok=True)
    os.makedirs(config.plots_dir, exist_ok=True)

def validate_input(data):
    # complex validation logic
    return True if data else False

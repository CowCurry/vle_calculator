import matplotlib.pyplot as plt
from config import config
import os
import pandas as pd

def plot_vle(df):
    os.makedirs(config.plots_dir, exist_ok=True)
    for comp in config.components:
        subset = df[df['y'].apply(lambda y: y.get(comp, 0))]
        plt.plot(subset['T'], subset['y'].apply(lambda y: y.get(comp,0)), label=comp)
    plt.xlabel('Temperature (K)')
    plt.ylabel('y')
    plt.title('Vapor-Liquid Equilibrium')
    plt.legend()
    plt.savefig(os.path.join(config.plots_dir, 'vle_plot.png'))
    plt.close()

def plot_phase_diagram(df):
    os.makedirs(config.plots_dir, exist_ok=True)
    plt.scatter(df['T'], df['P'], c='blue', marker='o')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Pressure (bara)')
    plt.title('Phase Diagram')
    plt.savefig(os.path.join(config.plots_dir, 'phase_diagram.png'))
    plt.close()

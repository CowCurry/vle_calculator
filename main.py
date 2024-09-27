from utils import initialize_directories
from data_loader import load_component_data
from equilibrium import solve_vle
from plotting import plot_vle, plot_phase_diagram
from config import config

def main():
    initialize_directories()
    components_data = load_component_data()
    if config.verbose:
        print("loaded component data")
    results = solve_vle()
    if config.verbose:
        print("solved VLE")
    plot_vle(results)
    plot_phase_diagram(results)
    if config.verbose:
        print("plots generated")

if __name__ == "__main__":
    main()

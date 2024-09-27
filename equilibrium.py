from thermodynamics import calculate_vle
from data_loader import generate_conditions
from config import config
import pandas as pd

def solve_vle():
    temperatures, pressures = generate_conditions()
    results = []
    for T in temperatures:
        for P in pressures:
            Psat = {comp: 1.0 for comp in config.components}  # placeholder
            y = calculate_vle(T, P, Psat)
            results.append({'T': T, 'P': P, 'y': y})
            if config.verbose:
                print(f"solved VLE for T={T} K, P={P} bara")
    df = pd.DataFrame(results)
    if config.save_results:
        df.to_csv(f"{config.results_dir}/vle_results.csv", index=False)
    return df

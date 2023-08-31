import os

input_folder = "./train"
output_folder = "./video"
cmd = f"""
python generate_forecasting_scenario_visualizations.py \
    --argoverse-scenario-dir={input_folder} \
    --viz-output-dir={output_folder} \
"""
print(cmd)
os.system(cmd)

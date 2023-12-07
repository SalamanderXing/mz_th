import os

input_folder = "../dataset/train"
output_folder = "../visualizations/"

cmd = f"""
python "./avi_scripts/generate_forecasting_scenario_visualizations.py" \
    --argoverse-scenario-dir={input_folder} \
    --viz-output-dir={output_folder} \
    --num-scenarios=2 \
"""
print(cmd)
os.system(cmd)

import pandas as pd

df = pd.read_parquet(
    "./train/01844147-17ff-4335-8186-c10c2b989260/scenario_01844147-17ff-4335-8186-c10c2b989260.parquet"
)

print(df)

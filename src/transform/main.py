import pandas as pd
import os

json_path = os.path.join(os.path.dirname(__file__), "../../data/data.json")

df = pd.read_json(json_path)
print(df.head())

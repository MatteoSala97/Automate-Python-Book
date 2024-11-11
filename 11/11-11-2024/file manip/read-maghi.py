import json
import pandas as pd

# Carica il file JSON in un DataFrame
filepath = r'C:\Users\matteo.sala\Documents\Automate Python Book\11\11-11-2024\maghi.json'
df = pd.read_json(filepath)

columns_to_modify = df.columns[df.columns != 'Nome_Mago']

df[columns_to_modify] = df[columns_to_modify].applymap(lambda x: "Owned" if x == 1 else "Not owned")

# print(df.to_string())
modified_data = df.to_dict(orient="records")

with open(filepath, 'w') as f:
    json.dump(modified_data, f, indent=4)

print("File JSON modificato con successo!")

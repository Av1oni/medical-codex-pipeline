import pandas as pd
from pathlib import Path

Input_file = Path(r"C:\Users\antho\Downloads\HHA 507\HHA-507-2025\assignments\medical-codex-pipeline\Input\icd10cm_order_2025.csv")
df = pd.read_csv(Input_file)

df['code'] = df['code'].str.strip()
df['description'] = df['description'].str.strip() 
df = df.drop_duplicates(subset=['code'])

output_file = Path("output/csv/icd10cm_clean.csv")
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print(f"Processed {len(df)} ICD-10-CM codes into {output_file}")

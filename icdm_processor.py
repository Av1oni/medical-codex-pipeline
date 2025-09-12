import pandas as pd
from pathlib import Path

input_file = Path("../input/icd10cm_raw.csv")
df = pd.read_csv(input_file)

df['code'] = df['code'].str.strip()
df['description'] = df['description'].str.strip() 
df = df.drop_duplicates(subset=['code'])

output_file = Path("../output/csv/icd10cm_clean.csv")
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print(f"Processed {len(df)} ICD-10-CM codes into {output_file}")

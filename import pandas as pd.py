import pandas as pd
from pathlib import Path

Input_file = Path("../input/hcpc2025_oct_anweb_v3.xlsx")
df = pd.read_csv(Input_file)

df['code'] = df['code'].str.strip()
df['description'] = df['description'].str.strip() 
df = df.drop_duplicates(subset=['code'])

output_file = Path("../output/csv/hcpc2025_anweb_clean.csv")
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print(f"Processed {len(df)} ICD-10-CM codes into {output_file}")

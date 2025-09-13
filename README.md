# HHA-507-2025
**HHA 507 Data Science Health Informatics 2025**

## Overview
This repository contains course materials, datasets, and code examples for HHA 507 Data Science in Health Informatics. The course focuses on practical data science applications in healthcare, working with medical coding systems, and health data analysis.

## Getting Started

### 1. Cloning the Repository
To get a local copy of this repository on your machine, use the following git commands:

```bash
# Clone the repository to your local machine
git clone https://github.com/yourusername/HHA-507-2025.git

# Navigate into the repository folder
cd HHA-507-2025

# Check the status of your local repository
git status
```

### 2. Basic Git Commands You'll Need
```bash
# Check if there are updates to download: 
git pull
```

### 3. Understanding .gitignore
The `.gitignore` file is crucial for this course because it tells Git which files to ignore and NOT upload to GitHub. This is especially important for:

#### Why We Use .gitignore:
- **Large Dataset Files**: Medical coding datasets (LOINC, ICD-10, HCPCS) can be 100MB+ and exceed GitHub's file size limits
- **Licensing Concerns**: Some medical datasets have usage restrictions and shouldn't be publicly shared
- **Repository Performance**: Keeps the repository lightweight and fast to clone/download
- **Privacy**: Prevents accidental upload of sensitive data files

#### What We're Ignoring:
Our .gitignore specifically excludes these large medical datasets:
- `Module1_MedicalCodexes/loinc/Loinc.csv` - LOINC laboratory codes (~50MB)
- `Module1_MedicalCodexes/icd/us/icd10cm_order_2025.txt` - ICD-10 diagnosis codes
- `Module1_MedicalCodexes/icd/who/icd102019syst_codes.txt` - WHO ICD-10 systematic names
- `Module1_MedicalCodexes/hcpcs/HCPC2025_OCT_ANWEB.txt` - HCPCS procedure codes

## Course Structure

### Module 1: Medical Codexes
Working with standard medical coding systems:
- **ICD-10**: International Classification of Diseases (diagnosis codes)
- **LOINC**: Logical Observation Identifiers Names and Codes (lab tests)
- **HCPCS**: Healthcare Common Procedure Coding System (procedures/supplies)

### Data Sources
Students will need to download these datasets separately from official sources:
- LOINC: https://loinc.org/downloads/
- ICD-10: https://www.cms.gov/medicare/coding-billing/icd-10-codes
- HCPCS: https://www.cms.gov/medicare/coding-billing/hcpcscode

## For Health Informatics Students

### Programming Expectations
This course assumes basic familiarity with:
- Python programming fundamentals
- Working with CSV/text files
- Basic data analysis concepts
- Command line/terminal usage

### Tools You'll Use
- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Jupyter Notebooks**: Interactive data exploration
- **Git/GitHub**: Version control and collaboration
- **VS Code**: Code editor

### Tips for Success
1. **Start Early**: Medical datasets are large and complex
2. **Documentation**: Keep detailed notes about your data processing steps
3. **Version Control**: Commit your work frequently with clear messages
4. **Collaboration**: Use GitHub issues and discussions to ask questions
5. **Data Privacy**: Always follow HIPAA and institutional guidelines when working with health data

### Common Issues and Solutions
- **Large File Errors**: If Git complains about file sizes, check that your datasets are properly listed in .gitignore
- **Memory Issues**: Large CSV files may require chunked processing in Python
- **Encoding Problems**: Medical data often uses different character encodings (UTF-8, Latin-1)

-----------------------------------------------------------------------------
# Step one
I created all my folders and downloaded the files i have access to through the links on your github

# 2
I then started with the ICD10 codes and I had a text file in my input and used the startup codes given to me to clean it and convert it to a csv file in the output folder.

# 3 
Looking at icd10cm_processor.py I imported the path of the orginal txt file

# 4 
Wrote a Python script process_codexes.py that:
1) Reads each file with pandas (read_csv for ICD, read_fwf for HCPCS).
2) Cleans whitespace and removes duplicate rows.
3) Saves the cleaned data to output/csv/ as CSV files.

# 5 
I then tested the pipeline by running the script and confirming that CSV files were generated in the output\csv file that I have

# 6 
When I was downloading the npi files the biggest one was already a csv file and I had some trouble figuring out what to do because when i clicked on it on input it said the file is too large to display in text.

# 7
The Npi keeps force shutting down my code so I will leave this as the last thing I do (it shut it down 3 times)

# 8
I finished my codes for each of the processor scripts however I keep getting an error saying no module named ... so I will submit this and update the git link when i figure out what is wrong
 
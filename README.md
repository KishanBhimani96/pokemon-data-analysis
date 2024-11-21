# Pokemon Data Analysis

A Python project analyzing Pokemon statistics to identify patterns in Attack, Defense, and Speed attributes across different Pokemon types.

## Features
- Analyzes Pokemon dataset with pandas
- Generates visualization of average Attack stats by Pokemon type
- Identifies top 10 strongest Pokemon by Attack stat
- Identifies top 10 fastest Pokemon by Speed stat

## Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn

## Installation
1. Clone this repository
2. Install required packages:
```bash
pip install pandas matplotlib seaborn
```

## Usage
Run the script:
```bash
python Pokemon_Data_Analysis.py
```
The script will:
- Download Pokemon dataset if not present
- Generate analysis
- Create visualization (saved as 'attack_by_type.png')
- Display top 10 strongest Pokemon

## Sample Output
The script generates:
- A bar plot showing average Attack statistics by Pokemon type
- Console output listing the top 10 strongest Pokemon

## Data Source
Pokemon dataset from Keith Galli's GitHub repository

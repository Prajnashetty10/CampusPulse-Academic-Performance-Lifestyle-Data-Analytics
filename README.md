# CampusPulse – Academic Performance & Lifestyle Data Analytics

## Project Overview
CampusPulse is a complete data analytics project.It analyzes academic and lifestyle factors to predict student performance and generate insights.

## Folder Structure
CampusPulse/
│
├── data/
│   └── student_data.csv
├── app/
│   └── analysis.py
├── models/
│   └── performance_model.pkl (generated after running)
├── requirements.txt
└── README.md

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

## Installation & Execution Steps

### Step 1: Install Python
Ensure Python 3.8 or above is installed.
Check version:
python --version

### Step 2: Open Project
Extract the ZIP file.
Open the CampusPulse folder in VS Code.

### Step 3: Install Dependencies
Open terminal inside project folder and run:
pip install -r requirements.txt

### Step 4: Run the Project
Execute the analysis script:
python app/analysis.py

Note: The script will create the `models/` folder automatically if it doesn't exist before saving the trained model.

### Step 5: Output
- Model R2 score will be displayed
- Trained model saved in models/performance_model.pkl

### Quick model verification
You can run a lightweight check to confirm the saved model can be loaded:

python scripts/check_model.py

If you want to run the pytest-based test (requires installing pytest):

pip install pytest
pytest -q

## Key Analytics Insights
- Attendance and study hours strongly influence GPA
- High stress and low sleep reduce performance
- Early identification of at-risk students is possible

## Suitable For
- Data Analyst Intern
- Junior Data Analyst
- Analytics Trainee

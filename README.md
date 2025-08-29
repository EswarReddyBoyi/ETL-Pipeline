ETL Pipeline using Pandas & Scikit-Learn

This project implements an ETL (Extract → Transform → Load) pipeline using Pandas and Scikit-Learn.
The pipeline automates dataset preprocessing including missing value handling, encoding categorical features, scaling numerical features, splitting into train/test sets, and saving processed data.

Features

Extract → Reads raw dataset (CSV).

Transform →

Handles missing values (SimpleImputer).

Scales numerical columns (StandardScaler).

Encodes categorical columns (OneHotEncoder).

Splits data into training/testing sets.

Load → Saves processed data as CSV files in processed_data/.

Project Structure
PROJECT/
│
├── etl_pipeline.py       # Main ETL script
├── README.md             # Documentation
├── titanic.csv           # Example dataset (raw data)
└── processed_data/       # Output folder with transformed datasets
    ├── X_train.csv
    ├── X_test.csv
    ├── y_train.csv
    └── y_test.csv

How to Run
1. Clone or download the project
git clone <your-repo-link>
cd PROJECT

2. Install dependencies
pip install pandas scikit-learn

3. Download example dataset

Titanic dataset (CSV):
Download Link

Save it as titanic.csv inside the project folder.

4. Run the pipeline
python etl_pipeline.py

✅ Output

After running, processed files will be saved in processed_data/:

X_train.csv → Training features

X_test.csv → Testing features

y_train.csv → Training labels

y_test.csv → Testing labels

🛠️ Customization

Change dataset file path inside etl_pipeline.py:

raw_file = "titanic.csv"
target_col = "Survived"


Replace with your dataset and target column.

Example

Using Titanic dataset (titanic.csv, target = Survived):

Raw shape: 891 rows × 12 columns

Transformed → Train/Test split (80/20).

Saved as new CSVs in processed_data/.
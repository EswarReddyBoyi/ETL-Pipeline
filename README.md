### ETL Pipeline using Pandas & Scikit-Learn

This project implements an ETL (Extract → Transform → Load) pipeline using Pandas and Scikit-Learn.
The pipeline automates dataset preprocessing including missing value handling, encoding categorical features, scaling numerical features, splitting into train/test sets, and saving processed data.

### Features

Extract → Reads raw dataset (CSV).

Transform →

Handles missing values (SimpleImputer).

Scales numerical columns (StandardScaler).

Encodes categorical columns (OneHotEncoder).

Splits data into training/testing sets.

Load → Saves processed data as CSV files in processed_data/.


### How to Run
### 1. Clone or download the project
````
git clone https://github.com/22BCE8093-Eswar/ETL-Pipeline
cd PROJECT
````

### 2. Install dependencies
````
pip install pandas scikit-learn
````

### 3. Download example dataset

Titanic dataset (CSV): https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv?utm_source=chatgpt.com

Save it as titanic.csv inside the project folder.

### 4. Run the pipeline
````
python etl_pipeline.py
````


**Output**

After running, processed files will be saved in processed_data/:

X_train.csv → Training features

X_test.csv → Testing features

y_train.csv → Training labels

y_test.csv → Testing labels

**Customization**

Change dataset file path inside etl_pipeline.py:
````
raw_file = "titanic.csv"
target_col = "Survived"
````

Replace with your dataset and target column.

**Example**

Using Titanic dataset (titanic.csv, target = Survived):

Raw shape: 891 rows × 12 columns

Transformed → Train/Test split (80/20).

Saved as new CSVs in processed_data/.

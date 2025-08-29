"""
ETL Pipeline: Data Preprocessing, Transformation, and Loading
Author: Boyi Eswar Reddy
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# ============== STEP 1: EXTRACT ===================
def extract_data(file_path: str) -> pd.DataFrame:
    """
    Reads raw CSV file into a pandas DataFrame.
    """
    print("📥 Extracting data...")
    df = pd.read_csv(file_path)
    print(f"Data shape: {df.shape}")
    return df


# ============== STEP 2: TRANSFORM ===================
def transform_data(df: pd.DataFrame, target_column: str):
    """
    Applies preprocessing: missing value imputation, encoding, scaling, and splitting.
    """
    print("🔄 Transforming data...")

    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Identify numerical and categorical columns
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = X.select_dtypes(include=['object']).columns

    # Numerical pipeline
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="mean")),  # handle missing numbers
        ('scaler', StandardScaler())  # scale numbers
    ])

    # Categorical pipeline
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="most_frequent")),  # handle missing categories
        ('encoder', OneHotEncoder(handle_unknown="ignore"))  # encode categorical
    ])

    # Combine pipelines
    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ])

    # Fit transform
    X_transformed = preprocessor.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_transformed, y, test_size=0.2, random_state=42
    )

    print("✅ Transformation complete.")
    return X_train, X_test, y_train, y_test, preprocessor


# ============== STEP 3: LOAD ===================
def load_data(X_train, X_test, y_train, y_test, output_dir="processed_data"):
    """
    Saves transformed datasets to CSV.
    """
    print("💾 Loading data...")

    import os
    os.makedirs(output_dir, exist_ok=True)

    # Convert back to DataFrame for saving
    X_train_df = pd.DataFrame(X_train.toarray() if hasattr(X_train, "toarray") else X_train)
    X_test_df = pd.DataFrame(X_test.toarray() if hasattr(X_test, "toarray") else X_test)

    y_train_df = pd.DataFrame(y_train).reset_index(drop=True)
    y_test_df = pd.DataFrame(y_test).reset_index(drop=True)

    # Save to CSV
    X_train_df.to_csv(f"{output_dir}/X_train.csv", index=False)
    X_test_df.to_csv(f"{output_dir}/X_test.csv", index=False)
    y_train_df.to_csv(f"{output_dir}/y_train.csv", index=False)
    y_test_df.to_csv(f"{output_dir}/y_test.csv", index=False)

    print(f"✅ Data saved in '{output_dir}/' folder.")


# ============== MAIN ETL FUNCTION ===================
if __name__ == "__main__":
    raw_file = "raw_data.csv"  # <-- Replace with your file
    target_col = "Survived"      # <-- Replace with your target column name

    df_raw = extract_data(raw_file)
    X_train, X_test, y_train, y_test, preprocessor = transform_data(df_raw, target_col)
    load_data(X_train, X_test, y_train, y_test)

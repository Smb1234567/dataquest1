Below is a sample README that help in explaining the data cleaning process:

---

## Data Cleaning Scripts

This repository includes a set of Python scripts that clean and preprocess four different datasets used in our project. The scripts leverage the [pandas](https://pandas.pydata.org/) library for data manipulation and are designed to remove inconsistencies and invalid data entries. Below is an overview of the cleaning steps performed for each dataset:

### 1. Movies Dataset

- **Loading Data:** The dataset is loaded from a CSV file (`movies.csv`).
- **Duplicate Removal:** Any duplicate records are removed.
- **Handling Missing Values:** Rows containing `NaN` values are dropped.
- **Saving:** The cleaned dataset is saved as `cleaned_movies.csv`.

### 2. Users Dataset

- **Loading Data:** The users' data is loaded from `users.csv`.
- **Duplicate Removal:** Duplicate entries are eliminated.
- **Column Pruning:** Unnecessary columns, such as `email`, are dropped.
- **Filtering Ages:** Only users with ages between 10 and 100 are retained to ensure realistic values.
- **Saving:** The processed dataset is written to `cleaned_users.csv`.

### 3. Ratings Dataset

- **Loading Data:** The ratings data is imported from `ratings.csv`.
- **Date Conversion:** The `review_date` field is converted to a datetime format to ensure consistency (note: the code snippet references `df` instead of `df_ratings` for this conversion, so ensure consistency in your final script).
- **Duplicate Removal:** Any duplicate rows are dropped.
- **Valid Range Enforcement:** Ratings are filtered to be within a valid range of 0 to 10.
- **Saving:** The final, cleaned dataset is saved as `cleaned_ratings.csv`.

### 4. Watch History Dataset

- **Loading Data:** The watch history data is read from `watch_history.csv`.
- **Duplicate Removal:** Duplicate entries are removed.
- **Valid Duration:** Only records with positive watch durations are retained.
- **Device Filtering:** The dataset is filtered to include only valid device types (e.g., Smartphone, Laptop, Tablet, Smart TV, Desktop, Gaming Console), thereby removing any irrelevant entries (like "washing machine").
- **Saving:** The cleaned dataset is saved as `cleaned_watch_history.csv`.

---

### How to Run

Each script is self-contained and uses `pandas` for data processing. Simply run the scripts in your Python environment to generate the cleaned CSV files.

---

This documentation provides a clear outline of the steps taken to ensure the datasets are ready for analysis, contributing to reproducible and reliable data-driven projects.

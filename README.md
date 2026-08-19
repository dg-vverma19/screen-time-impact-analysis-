# Screen Time Impact Analysis

**By Vivaan Verma**

This project explores the impact of screen time and how it correlates with education level, productivity level, attention span, and demographics. The project produces both exploratory data visualizations and machine learning model results.

## Required Installations

The project requires the following Python libraries:

- `pandas`
- `scikit-learn`
- `plotly`
- `mord`

Install them with:

```bash
pip install pandas scikit-learn plotly mord
```

## Files

### Data

- `[data_file.csv]` — The full dataset containing columns for screen time, education level, productivity level, attention span, and demographics.
- `[small_data_file.csv]` — A small subset of the data used only for conveniently testing the code.

### Code

- `eda.py` — Defines the exploratory data analysis functions used to generate and display visualizations exploring screen time across different variables.
- `screen_time_age_group.py` — Builds and evaluates the machine learning models used to analyze screen time patterns, printing model results and metrics.
- `eda_test.py` — A tester file that runs the exploratory visualizations on the smaller dataset to verify chart rendering.
- `age_screen_time_test.py` — A tester file that validates the metrics, calculations, and values used within the machine learning models.

## Instructions for Running

### 1. Install the Libraries

Install the four required libraries with:

```bash
pip install pandas scikit-learn plotly mord
```

if they are not already installed.

### 2. Place All Files in One Folder

Place the following files in the same folder:

- The four `.py` files
- The full `.csv` dataset
- The small `.csv` test dataset

### 3. Update File Paths

Each `.py` file has a path constant near the top. Replace this with the file path of the corresponding `.csv` file on your machine.

If the `.csv` files are in the same folder as the `.py` files, you can use only the file name.

- In `DATA_PATH`, set the path to `[data_file.csv]`.
- In `TEST_PATH`, set the path to `[small_data_file.csv]`.

### 4. Run `eda.py`

Run `eda.py` to generate the exploratory data visualizations.

You can either use the **Run** button in the top-right corner of your code editor or run the following command in the terminal:

```bash
python eda.py
```

### 5. Run `screen_time_age_group.py`

Run `screen_time_age_group.py` to summarize the machine learning results.

You can either use the **Run** button in the top-right corner of your code editor or run:

```bash
python screen_time_age_group.py
```

This will print the model output and metrics in the terminal.

### 6. Optional: Run `eda_test.py`

Run `eda_test.py` to generate test visualizations using the smaller dataset:

```bash
python eda_test.py
```

Use this file to check that the visualizations render correctly using the test dataset.

### 7. Optional: Run `age_screen_time_test.py`

Run `age_screen_time_test.py` to verify the calculations and model values:

```bash
python age_screen_time_test.py
```

Use this file to verify that the model values and calculations are running correctly.

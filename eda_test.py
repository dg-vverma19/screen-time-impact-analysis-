"""
Vivaan Verma
CSE 163 AC
This file checks the accuracy of the data filtering steps performed in 
eda.py on data.csv. 
"""

import pandas as pd


def test_data_accuracy(df: pd.DataFrame, group_cols: list[str]) -> None:
    """
    Checks that the grouped counts used in a visualization match the
    original dataset by comparing total row counts.
    """
    grouped = df.groupby(group_cols).size().reset_index(name='counts')
    print(grouped['counts'].sum() == len(df))


def main():
    df = pd.read_csv('data.csv')
    # Should all be true if code is correct
    test_data_accuracy(df, ['Average Screen Time', 'Productivity'])
    test_data_accuracy(df, ['Average Screen Time', 'Attention Span'])
    test_data_accuracy(df, ['Average Screen Time', 'Education Level'])


if __name__ == "__main__":
    main()

"""
Vivaan Verma
CSE 163 AC
This module contains multiple testing methods to ensure that
all model calculations are correct in age_group_screen_time.py
"""

import pandas as pd
from age_group_screen_time import (
    train_model,
    test_model,
    evaluate_model,
    screen_time,
    age_order,
    file_name
)
from sklearn.model_selection import train_test_split


def test_no_missing_mappings(df: pd.DataFrame) -> None:
    """
    This function checks that all the categorical values in the dataset
    were successfully converted into numbers. It takes in the dataframe,
    and makes sure no rows ended up empty or unmapped after converting
    Screen Time and Age Group into their ordinal versions.
    """
    df["Screen Time (ordinal)"] = df["Average Screen Time"].map(screen_time)
    df["Age Group (ordinal)"] = df["Age Group"].map(age_order)

    assert df["Screen Time (ordinal)"].isna().sum() == 0
    assert df["Age Group (ordinal)"].isna().sum() == 0
    print("test_no_missing_mappings passed")


def test_model_learns_all_classes(df: pd.DataFrame) -> None:
    """
    This function checks that the trained model is aware of every
    possible screen time category, not just some of them. It takes in
    the dataframe, trains a model on it, and confirms the model
    recognizes all six screen time brackets as valid outcomes.
    """
    df["Screen Time (ordinal)"] = df["Average Screen Time"].map(screen_time)
    df["Age Group (ordinal)"] = df["Age Group"].map(age_order)

    X = df[["Age Group (ordinal)"]]
    y = df["Screen Time (ordinal)"]
    model = train_model(X, y)

    assert set(model.classes_) == {0, 1, 2, 3, 4, 5}
    print("test_model_learns_all_classes passed")


def test_probabilities_sum_to_one(df: pd.DataFrame) -> None:
    """
    This function checks that the model's predicted probabilities are
    mathematically valid. It takes in the dataframe, trains a model,
    generates probability predictions for each age group, and confirms
    that each age group's probabilities add up to 100%, as they should.
    """
    df["Screen Time (ordinal)"] = df["Average Screen Time"].map(screen_time)
    df["Age Group (ordinal)"] = df["Age Group"].map(age_order)

    X = df[["Age Group (ordinal)"]]
    y = df["Screen Time (ordinal)"]
    model = train_model(X, y)
    trend, proba = evaluate_model(model)

    row_sums = proba.sum(axis=1)
    for total in row_sums:
        assert abs(total - 1.0) < 0.01
    print("test_probabilities_sum_to_one passed")


if __name__ == "__main__":
    df = pd.read_csv(file_name)
    test_no_missing_mappings(df)
    test_model_learns_all_classes(df)
    test_probabilities_sum_to_one(df)
    print("All tests passed")

"""
Vivaan Verma
CSE 163 AC
This module uses a dataset about screen time to create multiple methods
that follow the EDA requirements. These include, checking if the dataset
contains any empty values, creating a summary of each key column using
a dictionary, building a vertical bar plot comparing average screen time
to productivity, building a line plot comparing average screen time to
attention span, and building a horizontal bar plot comparing average
screen time to education levels.
"""

import pandas as pd
import plotly.express as px

file_name = "data.csv"
columns = [
    'Age Group',
    'Education Level',
    'Average Screen Time',
    'Productivity',
    'Attention Span'
]
screen_time_order = [
    'Less than 2', '2–4', '4–6', '6–8', '8-10', 'More than 10'
]


def empty_values(df: pd.DataFrame) -> bool:
    """
    Checks if the given DataFrame has any missing values
    """
    if df.isna().any().any():
        return True
    return False


def summary_columns(df: pd.DataFrame) -> dict[str, int]:
    """
    Uses the given DataFrame, and a list of columns to return
    a dictionary containing each unique value in each column,
    and a dictionary of how many times each unique value appears
    in each column. The keys in the dictionary are each col.
    """
    summary = {}

    # Go through each designated col:
    # Get the list of unique values in each col
    # Use values_count, and conver to a dict to return check how many
    # time each unique value appears in the column
    for col in columns:
        unique_values = list(df[col].unique())
        value_count = df[col].value_counts().to_dict()

        # For each key, store a tuple value
        summary[col] = (unique_values, value_count)

    return summary


def screen_time_to_productivity(df: pd.DataFrame) -> None:
    """
    This function uses the given DataFrame of Screen Time Usage,
    to compare how average screen time usage correlates with
    productivity by creating a vertical bar plot.
    """
    # Group data based on two columns creating a multindex
    # Take the size of that to get number of rows for each group
    # Change the name to the unnamed column, since .size() returns
    # a Series.
    filtered_data = df.groupby([
        'Average Screen Time',
        'Productivity'
    ]).size().reset_index(name='counts')

    fig = px.bar(
        filtered_data, x='Average Screen Time', y='counts',
        color='Productivity', barmode='stack',
        title='Screen time to Productivity',
        category_orders={'Average Screen Time': screen_time_order}
    )

    # Customization for Names
    fig.update_layout(
        xaxis_title='Number of Respondents',
        yaxis_title='Screen Time Bracket',
        legend_title='Productivity Level'
    )

    fig.write_html('screen_time_to_productivity.html')


def screen_time_to_attention_span(df: pd.DataFrame) -> None:
    """
    This function uses the given DataFrame of screen time usage in
    participants, to create a line plot comparing how average screen
    time affects attention span.
    """
    filtered_data = df.groupby([
        'Average Screen Time',
        'Attention Span'
    ]).size().reset_index(name='counts')

    fig = px.line(
        filtered_data, x='Average Screen Time', y='counts',
        color='Attention Span', markers=True,
        title='Screen Time to Attention Span',
        line_dash='Attention Span',
        line_shape='spline',
        category_orders={'Average Screen Time': screen_time_order}
    )

    fig.write_html('screen_time_to_attention_span.html')


def screen_time_to_education_level(df: pd.DataFrame) -> None:
    """
    This uses the given DataFrame of screen time usage in participants
    to create a horizontal bar plot comparing how average screen time
    differs in Education Levels.
    """
    filtered_data = df.groupby([
        'Average Screen Time',
        'Education Level'
    ]).size().reset_index(name='counts')

    fig = px.bar(
        filtered_data,
        y='Average Screen Time',
        x='counts',
        color='Education Level',
        orientation='h',
        barmode='stack',
        template='plotly_white',
        title='Average Screen Time based on Education Level',
        color_discrete_map={
            'High School or Below': 'purple',
            'Graduate': 'lightblue',
            'Undergraduate': 'red'
        },
        category_orders={'Average Screen Time': screen_time_order}
    )

    # Customization for Names
    fig.update_layout(
        xaxis_title='Number of Respondents',
        yaxis_title='Screen Time Bracket',
        legend_title='Education Level'
    )

    fig.write_html('screen_time_to_education_level.html')


def main():
    df = pd.read_csv(file_name)

    empty_or_not = empty_values(df)
    if empty_or_not:
        print('This dataset does not have any NaN values!')

    # Go through this dictionary, and print info for each col
    summary = summary_columns(df)
    for k in summary.keys():
        # Unpack the tuple
        values, counts = summary[k]

        print(f'\nFor this column {k}: \n')
        print(f'\nList of unique values: {values}\n')
        print(f'\nList of counts for each value {counts}')

    screen_time_to_productivity(df)
    screen_time_to_attention_span(df)
    screen_time_to_education_level(df)


if __name__ == "__main__":
    main()

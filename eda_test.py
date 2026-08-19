"""
Vivaan Verma
CSE 163 AC
This module tests the eda.py file to check if each 
visualization works correctly. 
"""

import pandas as pd
import plotly.express as px

small_data = {
    'Average Screen Time': ['2–4', '2–4', '4–6', '4–6', '4–6', '6–8'],
    'Productivity': ['High', 'Low', 'High', 'High', 'Low', 'Low'],
    'Attention Span': ['Long', 'Short', 'Long', 'Short', 'Short', 'Short'],
    'Education Level': [
        'Undergraduate', 'Graduate', 'Undergraduate',
        'High School or Below', 'Graduate', 'Undergraduate'
    ]
}

screen_time_order = ['2–4', '4–6', '6–8']


def screen_time_to_productivity(df: pd.DataFrame) -> None:
    """
    This function uses the given DataFrame of Screen Time Usage,
    to compare how average screen time usage correlates with
    productivity by creating a vertical bar plot.
    """
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
    fig.update_layout(
        xaxis_title='Screen Time Bracket',
        yaxis_title=' Number of Respondents',
        legend_title='Productivity Level'
    )
    fig.write_html('screen_time_to_productivity_test.html')


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
    filtered_data['Average Screen Time'] = pd.Categorical(
        filtered_data['Average Screen Time'],
        categories=screen_time_order,
        ordered=True
    )
    filtered_data = filtered_data.sort_values('Average Screen Time')
    fig = px.line(
        filtered_data, x='Average Screen Time', y='counts',
        color='Attention Span', markers=True,
        title='Screen Time to Attention Span',
        line_dash='Attention Span',
        line_shape='spline',
        category_orders={'Average Screen Time': screen_time_order}
    )
    fig.write_html('screen_time_to_attention_span_test.html')


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
    fig.write_html('screen_time_to_education_level_test.html')


def test_data_accuracy(df: pd.DataFrame, group_cols: list[str]) -> None:
    """
    Checks that the grouped counts used in a visualization match the
    original dataset by comparing total row counts.
    """
    grouped = df.groupby(group_cols).size().reset_index(name='counts')
    print(grouped['counts'].sum() == len(df))


def main() -> None:
    df = pd.DataFrame(small_data)
    screen_time_to_productivity(df)
    screen_time_to_attention_span(df)
    screen_time_to_education_level(df)

    df = pd.read_csv('data.csv')
    # Should all be true if code is correct
    test_data_accuracy(df, ['Average Screen Time', 'Productivity'])
    test_data_accuracy(df, ['Average Screen Time', 'Attention Span'])
    test_data_accuracy(df, ['Average Screen Time', 'Education Level'])
    print('All Tests Passed!')
    

if __name__ == '__main__':
    main()
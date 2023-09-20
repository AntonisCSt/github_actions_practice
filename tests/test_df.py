import pandas as pd

def create_dataframe():


    data = {'Name': ['George', 'Giannis', 'Charlie'],
            'Age': [25, 30, 35]}
    return pd.DataFrame(data)

def test_dataframe_column_names():


    df = create_dataframe()
    expected_columns = ['Name', 'Age']
    assert df.columns.tolist() == expected_columns,\
    "Column names are not as expected"


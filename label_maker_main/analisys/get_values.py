import pandas as pd


def get_values(excel_file) -> list:
    df = pd.read_excel(excel_file)
    data: list = df['code'].to_list()
    return data

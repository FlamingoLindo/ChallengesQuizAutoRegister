"""
Excel processing functions.
"""
import pandas as pd


def get_dataframe(xlsx_name):
    """
    Import an Excel file into a pandas DataFrame.

    Args:
        xlsx_name (str): Name of the Excel file to import

    Returns:
        pd.DataFrame: The imported DataFrame or empty DataFrame if error occurs
    """
    try:
        dataframe = pd.read_excel(xlsx_name)
        print(f"Successfully loaded {xlsx_name}")
        print(f"DataFrame shape: {dataframe.shape}")
        print(f"Columns: {dataframe.columns.tolist()}")
        return dataframe
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return pd.DataFrame()
    except ValueError as e:
        print(f"Value error: {e}")
        return pd.DataFrame()


def get_values_from_columns(dataframe, row_index=0):
    """
    Extract specific values from the main columns of a DataFrame row.

    Args:
        dataframe (pd.DataFrame): The DataFrame to extract values from
        row_index (int): The row index to extract values from (default: 0)

    Returns:
        tuple: (pergunta, alternativa_a, alternativa_b, alternativa_c, alternativa_d, 
                alternativa_correta, nivel_dificuldade, quantidade_pontos)

        Access it via: values[0], values[1], ..., values[7]
    """
    if dataframe.empty:
        print("DataFrame is empty.")
        return None

    if row_index >= len(dataframe):
        print(
            f"Row index {row_index} is out of range. DataFrame has {len(dataframe)} rows.")
        return None

    try:
        pergunta_text_local = dataframe.iloc[row_index, 0]  # PERGUNTA
        alternativa_a = dataframe.iloc[row_index, 1]  # ALTERNATIVA 1
        alternativa_b = dataframe.iloc[row_index, 2]  # ALTERNATIVA 2
        alternativa_c = dataframe.iloc[row_index, 3]  # ALTERNATIVA 3
        alternativa_d = dataframe.iloc[row_index, 4]  # ALTERNATIVA 4
        # ALTERNATIVA CORRETA
        alternativa_correta = dataframe.iloc[row_index, 5]
        # NÍVEL DE DIFICULDADE
        nivel_dificuldade = dataframe.iloc[row_index, 6]
        # QUANTIDADE DE PONTOS
        quantidade_pontos = dataframe.iloc[row_index, 7]

        print(dataframe.head())

        return pergunta_text_local, alternativa_a, alternativa_b, alternativa_c, \
            alternativa_d, alternativa_correta, nivel_dificuldade, quantidade_pontos

    except IndexError as e:
        print(f"Error accessing row {row_index}: {e}")
        return None

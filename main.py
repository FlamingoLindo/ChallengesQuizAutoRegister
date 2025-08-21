"""
Main function to run the Excel processing logic.
"""
from excel import get_dataframe, get_values_from_columns
from automate import automate_quiz_registration


def main():
    """
    Main function to run the Excel processing logic.
    """
    df = get_dataframe('example.xlsx')

    get_values_from_columns(df, row_index=0)

    automate_quiz_registration(
        '',
        '',
        '',
        df,
        categ_num=1,
        module_num=4,
        start_date_value='13082025'
    )


if __name__ == "__main__":
    main()

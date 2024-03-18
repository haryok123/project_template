import pandas as pd


def input_text_from_console():
    """
    Function to input text from the console.

    Returns the text entered by the user.
    """
    user_input = input("Enter text: ")
    return user_input


def read_text_from_file(file_path):
    """Reads text from a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The text read from the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: If an error occurs while reading the file.
    """

    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.") from e
    except Exception as e:
        raise Exception(f"Error reading file '{file_path}': {e}") from e


def read_text_from_file_with_pandas(file_path):
    """Function to read text from a file using the Pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The text read from the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        pd.errors.EmptyDataError: If the specified file is empty.
        pd.errors.ParserError: If there is an issue parsing the file.
        Exception: If any other error occurs while reading the file.
    """

    try:
        data = pd.read_csv(file_path)
        text = data.to_string(index=False, header=False)
        return text
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.") from e
    except pd.errors.EmptyDataError as e:
        raise pd.errors.EmptyDataError(f"Error: File '{file_path}' is empty.") from e
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Error: Unable to parse file '{file_path}'.") from e
    except Exception as e:
        raise Exception(f"Error reading file '{file_path}': {e}") from e

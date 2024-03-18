

def output_text_to_console(text):
    """Function to output text to the console.

    Args:
        text: any object or data to be printed in a console.
    """
    print(text)


def write_text_to_file(file_path, data):
    """Function to write data to a file using Python's built-in capabilities.

    Args:
        data (any): any object or data to write in a file.
        file_path (string): path to a file to write in.
    """
    with open(file_path, 'w') as file:
        file.write(data)

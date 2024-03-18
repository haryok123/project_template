from app.io.input import input_text_from_console, read_text_from_file, read_text_from_file_with_pandas
from app.io.output import output_text_to_console, write_text_to_file


def main():
    user_input = input_text_from_console()
    file_text = read_text_from_file("data/file.txt")
    pandas_text = read_text_from_file_with_pandas("data/file.csv")

    output_text_to_console("User input:\n" + user_input)
    output_text_to_console("\nText from file.txt:\n" + file_text)
    output_text_to_console("\nText from file.csv:\n" + pandas_text)

    write_text_to_file("output.txt", "User input:\n" + user_input + "\n\nText from file.txt:\n" + file_text + "\n\nText from file.csv:\n" + pandas_text)


if __name__ == "__main__":
    main()

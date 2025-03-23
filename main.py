import sys
from stats import get_book_text_count, get_char_counts, generate_book_report


def get_book_text(path_to_file):
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])

    get_book_text_count(file_contents)

    char_counts = get_char_counts(file_contents)

    generate_book_report(char_dict=char_counts, text=file_contents)


main()

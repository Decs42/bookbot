import sys
from stats import (
    get_book_text_count,
    get_char_counts,
    generate_book_report,
    get_book_text,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])

    words_count = get_book_text_count(file_contents)

    char_counts = get_char_counts(file_contents)

    generate_book_report(
        char_dict=char_counts, words_count=words_count, book_path=sys.argv[1]
    )


main()

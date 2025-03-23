def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def get_book_text_count(text: str):
    split_text = text.split()
    return len(split_text)


def get_char_counts(text: str):
    char_dict = {}

    text = text.lower()

    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict


def sorting_func(dict: dict):
    return dict["count"]


def generate_book_report(char_dict: dict, words_count: int, book_path: str):
    new_list = []

    for char in char_dict:
        if char.isalpha():
            count = char_dict[char]
            list_dict = {"char": char, "count": count}
            new_list.append(list_dict)

    new_list.sort(reverse=True, key=sorting_func)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in new_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

def get_book_text_count(text):
    split_text = text.split()
    return f"{len(split_text)} words found in the document"


def get_char_counts(text):
    char_dict = {}

    for word in text:
        for char in word:
            lowercase_char = char.lower()
            if lowercase_char not in char_dict:
                char_dict[lowercase_char] = 1
            else:
                char_dict[lowercase_char] += 1

    return char_dict


def generate_book_report(char_dict, text):
    new_list = []
    split_text = text.split()

    def sorting_func(dict):
        return dict["count"]

    for char in char_dict:
        if char.isalpha():
            print(char)
            count = char_dict[char]
            list_dict = {"char": char, "count": count}
            new_list.append(list_dict)

    new_list.sort(reverse=True, key=sorting_func)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(split_text)} total words")
    print("--------- Character Count -------")
    for item in new_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

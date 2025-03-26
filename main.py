import sys
from stats import get_word_count, get_letter_count, sort_letter_dicts

def get_book_text(filePath):
    print(f"Analyzing book found at {filePath}")
    file_contents = ""

    with open(filePath, encoding='utf-8', errors='ignore') as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    letter_count_dict = get_letter_count(book_text)
    sorted_letter_dicts = sort_letter_dicts(letter_count_dict)

    print("--------- Character Count -------")
    for dict in sorted_letter_dicts:
        print(f"{dict['letter']}: {dict['count']}")
    print("============= END ===============")


main()




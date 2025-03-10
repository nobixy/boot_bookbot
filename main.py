import sys
from stats import get_num_words, count_chars, report

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_of_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("---------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("------- Character Count -------")
    report_dict = report(count_chars(text))
    for item in report_dict:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f'{char}: {count}')
    print("============ END ============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

def get_num_words(book):
    book_list = book.split()
    book_word_length = len(book_list)
    return book_word_length

def count_chars(book):
    book_list = book.split()
    char_occ = {}

    for word in book_list:
        for char in word:
            char = char.lower()
            if char in char_occ:
                char_occ[char] += 1
            else:
                char_occ[char] = 1

    return char_occ

def report(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]

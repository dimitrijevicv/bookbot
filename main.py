def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_list = build_list(chars_dict)
    sorted = sort_dict(dict_list)
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{num_words} words found in the document")
    print()
    for dict in sorted:
        cchar = dict["letter"]
        ccount = dict["num"]
        print(f"The '{cchar}' character was found {ccount} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def build_list(dict):
    list_dict = []
    for each in dict:
        if each.isalpha():
            list_dict.append({"letter": each, "num": dict[each]})
    return list_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict_list):
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


main()
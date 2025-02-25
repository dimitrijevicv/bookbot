def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    def get_num_words(text):
        words = text.split()
        return len(words)

    def get_book_text(path):
        with open(path) as f:
            return f.read()
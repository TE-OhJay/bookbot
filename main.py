def get_book_text(file_path):
    with open(file_path) as content:
        return content.read()


def word_counter(file_path):
    num_words = len(get_book_text(file_path).split())
    return f"{num_words} words found in the document"


def main():
    print(word_counter("./books/frankenstein.txt"))
    #print(get_book_text("./books/frankenstein.txt"))
    
main()
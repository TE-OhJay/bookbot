from stats import get_num_words

def get_book_text(file_path):
    with open(file_path) as content:
        return content.read()


def main():
    #text stores data for interaction with word_count
    text = (get_book_text("./books/frankenstein.txt"))
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")
    
main()
from stats import word_counter

def get_book_text(file_path):
    with open(file_path) as content:
        return content.read()


def main():
    print(word_counter("./books/frankenstein.txt"))
    #print(get_book_text("./books/frankenstein.txt"))
    
main()
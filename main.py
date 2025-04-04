import sys
from stats import get_num_words, count_characters, sort_characters


def get_book_text(file_path):
    with open(file_path) as content:
        return content.read()


def main():
    if len(sys.argv[:]) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    #text stores data for interaction with word_count
    text = (get_book_text(sys.argv[1]))
    
    
    print("----------- Word Count ----------")
    #word_count counts the number of words in text.
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    
    
    
    print("--------- Character Count -------")
    #character_count simply counts all the characters in text, including symbols and spaces.
    character_count = count_characters(text)
    #character_sort simply sorts the character_count by nr. of appearance
    character_sort = sort_characters(character_count)

    for entry in character_sort:
        if entry["character"].isalpha():
            print(f"{entry["character"]}: {entry["count"]}")
    
    print("============= END ===============")


main()
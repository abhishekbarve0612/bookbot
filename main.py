import sys
from stats import get_word_count, get_each_character_count
from utils import sort_arr

def get_book_text(file_path):
    with open(file_path) as file:
        file_text = file.read()
        return file_text
       
def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(args[1])
    num_words = get_word_count(content)
    # print(f"{num_words} words found in the document")
    each_character_count = get_each_character_count(content)
    sorted_characters_count = sort_arr(each_character_count)
    # words_count = get_each_word_count(content)
    # sorted_words_count = sort_arr(characters_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for charac in sorted_characters_count:
        if charac['char'].isalpha():
            print(f"{charac['char']}: {charac['count']}")
    print("============= END ===============")

main()
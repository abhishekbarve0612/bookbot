from stats import get_word_count, get_each_character_count

def get_book_text(file_path):
    with open(file_path) as file:
        file_text = file.read()
        return file_text
       
def main():
    content = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(content)
    # print(f"{num_words} words found in the document")
    each_character_count = get_each_character_count(content)
    print(each_character_count)

main()
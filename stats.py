def get_word_count(text):
    return len(text.split())

def get_each_character_count(text):
    text = text.lower()
    char_set = set(text)
    char_count = {}
    for char in char_set:
        char_count[char] = text.count(char)
    return char_count
    
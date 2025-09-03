def get_word_count(text):
    return len(text.split())

def get_each_character_count(text):
    text = text.lower()
    char_set = set(text)
    char_count = []
    for char in char_set:
        char_count.append({
            "char": char,
            "count": text.count(char)
        })
    return char_count
    
def get_each_word_count(text):
    text = text.lower()
    words = text.split()
    word_counts = []
    for word in words:
        word_counds.append({
            "word": word,
            "count": words.count(word)
        })
    return word_counts
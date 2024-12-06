def main():
    book_path = "bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    report = get_report(text)
    print(report)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char = {}
    for c in text:
        lowered = c.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1
    return char

def get_report(text):
    char_dict = get_char_dict(text)
    print('--Begin report --')
    for key, in char_dict:
        print(f'The {key} character was found {char_dict[key]} times')
    print('-- End Report --')


main()

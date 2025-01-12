book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    print_report(text)
        
def count_words(text):
    words = text.split()
    return (len(words))

def count_characters(text):
    l = text.lower()
    letter_counts = {}
    if not l:
        return letter_counts
    for character in l:
        letter_counts[character] = letter_counts.get(character, 0) + 1
    return letter_counts

def make_list(text):
    char_dict = count_characters(text)
    new_dict = {}
    dict_list = []
    test = {}
    for char in char_dict:
        if char.isalpha():
            new_dict = {"letter" : char, "count" : char_dict[char]}
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list

    

def sort_on(dict):
    return dict["count"]

def print_report(text):
    dict_list = make_list(text)
    num_words = count_words(text)

    print(f"--- Begin report on {book_path}. ---")
    print(f"{num_words} words were found in the analyzied text.\n")
    #if dict_list:
    for item in dict_list:
        letter = item["letter"]
        count = item["count"]
        print(f"The letter '{letter}' was found {count} times.")
    print(f"--- End report on {book_path} ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
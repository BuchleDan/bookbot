book_path = "books/alum_1_50.txt"

def main():
    text = get_book_text(book_path)
    print_report(text)
        
def count_words(text):
    words = text.split()
    return (len(words))

def words_found(text):
    words = text.split()
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    
    return words_dict

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
    for char in char_dict:
        if char.isalpha():
            new_dict = {"letter" : char, "count" : char_dict[char]}
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list

def make_word_list(text):
    word_dict = words_found(text)
    word_list = []
    for word in word_dict:
        new_dict = {"word" : word, "count" : word_dict[word]}
        word_list.append(new_dict)
    word_list.sort(reverse=True, key=sort_on)
    
    return word_list

def sort_on(dict):
    return dict["count"]

def print_report(text):
    dict_list = make_list(text)
    word_list = make_word_list(text)
    num_words = count_words(text)
    with open("output.txt", "a") as f:
        print(f"--- Begin report on ALuM. ---", file=f)
        print(f"{num_words} words were found in the analyzied text.\n", file=f)
        #if dict_list:
        for item in dict_list:
            letter = item["letter"]
            count = item["count"]
            print(f"The letter '{letter}' was found {count} times.", file=f)
        print("\n===================================================\n", file=f)
        for w in word_list:
            word = w["word"]
            count = w["count"]
            print(f"The word '{word}' was found {count} times.", file=f)
        print(f"--- End report on ALuM ---", file=f)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
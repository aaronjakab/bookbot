def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = sort_chars(text)
    print_report(char_count, num_words, book_path)

def sort_chars(text):
    char_count = get_char_count(text)
    myVals = list(char_count.values())
    char_list = []
    for i in char_count:
        if i.isalpha():
            val = char_count[i]
            char_list.append({'char':i, "count" : val})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
def sort_on(dict):
    return dict["count"]
    
def print_report(dict, num_words, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for i in dict:
        val = i["count"]
        char = i["char"]
        print(f"The '{char}' character was found {val} times")




def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    lowered_text = text.lower()
    char_dict = {}
    for c in lowered_text:
        if char_dict.get(c) != None:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict



main()
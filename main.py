def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = get_char_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['count']} times")

    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["count"]

def get_char_sorted_list(count_chars_dict):
    sorted_list = []
    for char, count in count_chars_dict.items():
        sorted_list.append({"character": char, "count": count})
    sorted_list.sort(key=sort_on, reverse=True)    
    return sorted_list
   

main()

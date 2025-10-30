def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def count_book_words(book_text):
    book_splitted = book_text.split()

    return len(book_splitted)

def count_chars(book_text):
    alph_chars = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower in alph_chars:
            alph_chars[char_lower] += 1
        else:
            alph_chars[char_lower] = 1
    return alph_chars

def sort_on(dict_item):
    return dict_item["num"]

def dict_char_sort(alph_chars):
   dict_list = []
   for char in alph_chars:
       new_char = {"char":char,"num":alph_chars[char]}
       dict_list.append(new_char)

   dict_list.sort(reverse=True, key=sort_on) 
   return dict_list


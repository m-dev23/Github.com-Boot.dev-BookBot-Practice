from stats import count_book_words, count_chars, get_book_text, dict_char_sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        count_words = count_book_words(get_book_text(path))
        #print(f"Found {count_words} total words")
        total_chars = count_chars(get_book_text(path))
        new_list = dict_char_sort(total_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words} total words")
        print("--------- Character Count -------")
        for item in new_list:
            if item["char"].isalpha():
                print(item["char"]+": "+ str(item["num"]))
            
        print("============= END ===============")

main()
#total_chars = count_chars(get_book_text(path))

#print(total_chars)

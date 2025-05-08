import sys
from stats import number_of_words,number_of_characters,list_of_chars
def  get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def main():
    if len(sys.argv)==1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words=number_of_words(book_text)
    num_char=number_of_characters(book_text)
    list_char=list_of_chars(num_char)
    print(list_char,"l2")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_char:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
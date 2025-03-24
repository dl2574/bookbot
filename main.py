import sys
from stats import word_count, character_count, sorted_characters

def get_book_text(file_path):
    file_string = ""
    with open(file_path) as file:
        file_string = file.read()

    return file_string


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    text = get_book_text(path)
    wc = word_count(text)
    cc = character_count(text)
    sorted_cc = sorted_characters(cc)
  
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for dict in sorted_cc:
        print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")

main()


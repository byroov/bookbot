import sys
from stats import dict_sort, get_character_count, get_num_words




if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]


def get_book_text(path):
    with open(path) as f:
        file = f.read()
        return file
    
def main(path):
    text_str = get_book_text(path)
    print(text_str)


words = get_num_words(get_book_text(path))
text = get_book_text(path)
character_count = get_character_count(text)
alpha_chars = dict_sort(character_count)


print("============ BOOKBOT ============") 
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {words} total words")
print("--------- Character Count -------")
for item in alpha_chars:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")
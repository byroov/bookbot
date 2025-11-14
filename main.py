path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        file = f.read()
        return file
    
def main(path):
    text_str = get_book_text(path)
    print(text_str)

text = get_book_text(path)

def get_wordcount(text):
   num_words =len(text.split())
   print(f"Found {num_words} total words")



get_wordcount(text)

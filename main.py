from stats import count_words, count_characters

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  book_text = get_book_text("./books/frankenstein.txt")
  number_of_words = count_words(book_text)
  characters = count_characters(book_text)
  print(f"Found {number_of_words} total words")
  print(characters)


main()
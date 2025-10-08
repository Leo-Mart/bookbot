from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  number_of_words = count_words(book_text)
  characters = count_characters(book_text)
  sorted_list = sort_dict(characters)

  print("============ BOOKBOT ============\n")
  print(f"Analyzing book found at {book_path}\n")
  print("----------- Word Count ----------\n")
  print(f"Found {number_of_words} total words\n")
  print("--------- Character Count -------\n")
  for item in sorted_list:
    print(f"{item["char"]}: {item["num"]}\n")

main()
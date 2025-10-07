def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
  characters = {}

  for char in text:
    lowercase_char = char.lower()
    if lowercase_char in characters:
      characters[lowercase_char] += 1
    else:
      characters[lowercase_char] = 1

  return characters
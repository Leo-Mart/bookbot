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

def sort_dict(dict):
  def sort_on(items):
    return items["num"]
  
  list = []
  new_dict = {}
  for item in dict:
    if item.isalpha() == False:
      continue
    new_dict = {"char": item, "num": dict[item]}
    list.append(new_dict)

  list.sort(reverse=True, key=sort_on)

  return list

  

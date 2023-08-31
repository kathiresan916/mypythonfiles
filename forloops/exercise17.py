#Without Vowels words:

def count_words_without_vowels(string):
  """Counts the number of words in a string that do not contain any vowels.

  Args:
    string: The string to be counted.

  Returns:
    The number of words in the string that do not contain any vowels.
  """
  words = string.split()
  count = 0

  for word in words:
    vowels = "aeiou"
    for char in word:
      if char.lower() in vowels:
        break
    else:
      count += 1

  return count


if __name__ == "__main__":
  string = input("Enter String: ")
  print(count_words_without_vowels(string))


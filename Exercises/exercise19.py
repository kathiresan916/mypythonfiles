"""Emoji Converter"""

user_input = input(">")
words = user_input.split(' ')
emoji = {
    ":)": "😊",
    ":(": "😢"
}
OUTPUT = ""
for word in words:
    OUTPUT += emoji.get(word, word)+" "
print(OUTPUT)

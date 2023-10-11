"""Emoji Convertor"""


def emoji_convertor(message):
    """Emoji Convertor"""
    words = message.split(" ")
    emoji = {
        ":)": "😊",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("Type Here: ")
print(emoji_convertor(message))

# Daily Basis Check

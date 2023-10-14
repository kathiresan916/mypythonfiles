"""Emoji Convertor"""


def emoji_convertor(input_message_1):
    """Emoji Convertor"""
    words = input_message_1.split(" ")
    emoji = {
        ":)": "😊",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message_1 = input("Type Here: ")
print(emoji_convertor(message_1))

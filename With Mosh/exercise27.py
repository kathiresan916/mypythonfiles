#Image_Convertor using Function:

def emoji_convertor(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_convertor(message))

"""
messages = message.split(' ')

emojis = {
    ":)" : "😊",
    ":(" : "😢"
}

output = ""
for emoji in messages:
    output += emojis.get(emoji, emoji) + " "

"""
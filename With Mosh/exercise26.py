#Emoji'Series

message = input(">")

messages = message.split(' ')

emojis = {
    ":)" : "😊",
    ":(" : "😢"
}

output = ""
for emoji in messages:
    output += emojis.get(emoji, emoji) + " "

print(output)

"""Dictionaries"""

my_details = {
    "Name": "Kathiresan Selvaraj",
    "Birth Date": "02/09/1995",
    "Qualification": "BCA",
    "Father Name": "Selvaraj",
    "Mother Name": "Rasakani",
    "Favorite": "Spiritual Events"
}
KEYS_TO_SEARCH = ("Name", "Birth Date", "Qualification",
                  "Father Name", "Mother Name", "Favorite")
key = input("Enter Get your Data: ")
for key in KEYS_TO_SEARCH:
    print(f"{key}: {my_details.get(key)}")

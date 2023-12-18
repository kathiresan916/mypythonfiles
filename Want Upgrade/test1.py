# Read & Write

from docx import Document

with open("Test.docx", "w") as file:
    file.write("Modified")

with open("Test.docx", "r") as file:
    content = file.read()
    print(content)
    

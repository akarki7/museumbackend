import re
from docx import Document

document = Document('file.docx')
patterns = [
    "Current Number",
    "Title",
    "Name of file",
    "Item / photo / video / audio / document",
    "Original or scan / copy",
    "Where is the original",
    "Time period (Flakkaserne and before / Grohn Barracks I / DP Camp Grohn / Grohn Barracks II / Roland-Kaserne / IUB-JU)"
    "When produced",
    "Where produced",
    "By whom produced (author)",
    "Size",
    "Description",
    "Source",
    "Signature",
    "Copyright situation",
    "Where is the object now",
    "Found by",
    "Found when",
    "Date of production of the object sheet",
    "Additional information",
]
matches = {}
filtered_paragraphs = list(filter(lambda x: len(x.text) != 0, document.paragraphs))
for pattern in patterns:
    for index, para in enumerate(filtered_paragraphs):
        pos=para.text.find(pattern)
        if pos != -1:
            matches[pattern] = filtered_paragraphs[index + 1].text
print(matches)   
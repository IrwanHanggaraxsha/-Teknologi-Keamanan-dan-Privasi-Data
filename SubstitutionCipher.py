alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "fcpevqkzgmtrayonujdlwhbxsi"
text = "axsha ganteng banget"

result = ""
for letter in text:
    if letter.lower() in alphabet:
        result += key[alphabet.find(letter.lower())]
    else:
        result += letter

print(result)

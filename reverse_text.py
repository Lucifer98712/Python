def reverse_text_junior(text):
    return "".join(reversed(text))

def reverse_text_senior(text):
    return text[:: -1]

inputText = input("Enter text to be reversed: ")
revTextJun = reverse_text_junior(inputText)
revTextSen = reverse_text_senior(inputText)
print('Jun: ' + revTextJun + ' Sen: ' + revTextSen)
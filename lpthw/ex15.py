from sys import argv
script,filename = argv

text = open(filename)

print(f"Here's your file {filename}:")
print(text.read())

print("Type the filename again:")
file_again = input("> ")

text_again = open(file_again)

print(text_again.read())

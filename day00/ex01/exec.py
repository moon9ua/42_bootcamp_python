import sys

text = ""

for i in range(1, len(sys.argv)):
	if text == "":
		text = sys.argv[i]
	else:
		text = text + " " + sys.argv[i]
	i = i + 1

new_text = ""

for i in range(len(text) - 1, -1, -1):
	if text[i].isupper() == True:
		new_text = new_text + text[i].lower()
	else:
		new_text = new_text + text[i].upper()
	i = i - 1

print(new_text)
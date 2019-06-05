import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys()))>0:
		yn = raw_input("Did you mean %s instead?\nEnter y if yes, n if no:" % get_close_matches(w,data.keys())[0])
		if yn == 'y':
			return data[get_close_matches(w,data.keys())[0]]
		elif yn == 'n':
			return "Word not found."
		else:
			return "Invalid input."
	else:
		return "Word not found."

word = raw_input("Enter a word:")

output = translate(word)

if type(output) == list: #to avoid strings we are returning as errors or prompts
	for item in output:
		print(item)
else:
		print(output)
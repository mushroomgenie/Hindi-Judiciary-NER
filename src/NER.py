# -*- coding: utf-8 -*-
import sys,re
# from HindiTokenizer import Tokenizer
text= raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
# t = Tokenizer(text)
newline = text.replace(u"\'", "")
newline = newline.replace(u"(", "")
newline = newline.replace(u")", "")
newline = newline.replace(u"/", "")
newline = newline.replace(u",", "")
newline = newline.replace(u".", "")
# newline = newline.replace("-", "")
words = newline.split(u" ")

#newline= re.sub(r'\'', '', line)

newline= re.findall('[a-zA-Z0-9]+', newline)
final_str = ""
newline= " ".join(newline)
final_str+=newline
final_str+='\n'
# words = t.tokenize()
# t.print_tokens
file = open("../Data/tokenized-hindi","r+")
lines = file.readlines()
rules = dict()
for line in lines:
	if line[0] == "<":
		continue
	tokens = line.split()
	if len(tokens) == 3:
		continue
	else:
		if tokens == []:
			continue

		if tokens[1] in rules.keys():
			continue
		else:
			rules[tokens[1]] = tokens[3]

# for i in rules.keys():
	# print(i,rules[i])
gazette_list = [u"जनवरी",u"फ़रवरी",u"मार्च",u"अप्रैल",u"मई",u"जून",u"जुलाई",u"अगस्त",u"सितंबर",u"अक्टूबर",u"नवंबर",u"दिसंबर"]
op = ""
for word in range(len(words)):
	# print(tokens)
	if words[word] == u"संविधान" and words[word+2] == u"संशोधन":
		words[word+1] += "/B-Amendment"
		words[word+2] += "/I-Amendment"
	elif words[word] == u"अनुच्छेद":
		pass	
	elif words[word] == u"धारा":
		words[word] += "/B-Section"
		words[word+1] += "/I-Section"
	elif words[word] == u"द्वारा":
		words[word+1] += "B-Time"
	elif words[word] in [gazette_list]:
		words[word-1] += "/B-Time"
		words[word] += "/I-Time"
		words[word+1] += "/I-Time"
	else:# words[word] in rules.keys():
		for key in rules.keys():
			if key.decode('utf-8') == words[word]:
				words[word] += '/'+rules[key]
	

for word in words:
	print(word)
	op=op+word+" "

print("\n"+op+"\n")

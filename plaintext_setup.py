import re
text ="""

"""

text = text.lower() 

r = re.compile('[^a-z]')
text = r.sub("", text)
print(len(text))

text_file = open("Moby_Dick.txt", "w")
n = text_file.write(text)
text_file.close()
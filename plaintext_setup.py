import re
text ="""
"""

text = text.lower() 

r = re.compile('[^a-z]')
text = r.sub("", text)
print(len(text))

text_file = open("Tom_Sawyer.txt", "w")
n = text_file.write(text)
text_file.close()
import re

with open('./kinglear/kinglear.txt', 'r') as f:
    text = f.read()
matches = re.sub(r'([A-Z][A-Z]+[,\.]?)|(Fool)|([Ll]ord)', '', text)

filewrite = open('./kinglear/klmodified.txt', 'w')
filewrite.write(matches)
filewrite.close()
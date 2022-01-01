import re
from nltk.tokenize import RegexpTokenizer
# content=""
# with open('Test.lang','r') as file:
#     content = file.read()
# tokenizer = RegexpTokenizer("[\w]+|\n|\.|\"|\'|,|\{|\}|\(|\)|\=|;|:|\[|\]")
# tokens = tokenizer.tokenize(content)
# print(tokens)
hi = input()
if re.match("^.*$",hi):
    print("true")
else:
    print("false")
import re
from nltk.tokenize import RegexpTokenizer
motscles = "class|String|int|char|float|Scanner|nextInt|nextFloat|nextLine|System|out|println|if|else|public|static|void|new|^in$"
operateurs = "^(=)$|^(\+){1,2}$|^(-)$|^(<)$|^(>)$"
entier = "^(\d+)$"
reel = "^(\d+)\.(\d+)$"
symboles = "[\[!\|{};,\.']|\(\){|\(|\)|{}|\[\]|\{|\}|\"|\?"
identif = "^[a-zA-Z_]+[a-zA-Z0-9_]*$"
stringvar = ' *[\']{1} *[A-za-z0-9]+ *[\']{1}$ | *[\"]{1} *[A-za-z0-9]+ *[\"]{1}$'
Space = "\n"

class lexer(object):
    
    def __init__(self,source_code):
        self.source_code = source_code
        
    def tokenize(self):
        #all the content created by lexer will be stored here
        tokens=[]
        content=""
        with open('Test.lang','r') as file:
            content = file.read()
            tokenizer = RegexpTokenizer("[\w]+|\n|\.|\"|\'|,|\{|\}|\(|\)|\=|;|:|\[|\]|>|<|-|!")
            token_list = tokenizer.tokenize(content) 
        print(token_list)
        for word in token_list:
            if(re.findall(motscles,word)):
                if word=='class':
                    tokens.append(["CLASS",word])
                elif word =='float':
                    tokens.append(["FLOAT_DECLARATION",word])
                elif word == 'char':
                    tokens.append(["CHAR_DECLARATION",word])
                elif word == 'int':
                    tokens.append(["INT_DECLARATION",word])
                elif word == 'Scanner':
                    tokens.append(["SCANNER",word])
                elif word == 'println':
                    tokens.append(["PRINT",word])
                elif word == 'if':
                    tokens.append(["IF_STAT",word])
                elif word == 'else':
                    tokens.append(["ELSE_STAT",word])
                elif word == 'new':
                    tokens.append(["NEW",word])
                elif word == 'nextInt':
                    tokens.append(["NEXT_INT",word])
                elif word == 'nextFloat':
                    tokens.append(["NEXT_FLOAT",word])
                elif word == 'nextLine':
                    tokens.append(["NEXT_LINE",word])
                elif word == 'System':
                    tokens.append(["SYSTEM",word])
                elif word == 'out':
                    tokens.append(["OUT",word])
                elif word == 'in':
                    tokens.append(["IN",word])
                elif word == 'String':
                    tokens.append(["STRING_DECLARATION",word])
                elif word == 'public':
                    tokens.append(["PUBLIC",word])
                elif word == 'void':
                    tokens.append(["VOID",word])
                elif word == 'static':
                    tokens.append(["STATIC",word])
            
            elif(re.findall(identif,word)):
                tokens.append(['IDENTIF',word])
            elif(re.findall(stringvar,word)):
                    tokens.append(['STRING',word])
            elif(re.findall(operateurs,word)):
                tokens.append(['OPERATEUR',word]) 
            elif(re.findall(entier,word)):
                tokens.append(['NUMBER',word])
            
            elif word=="\n":
                tokens.append(['NEWLINE',word]) 
            elif(re.findall(symboles,word)):
                if word =='{':
                    tokens.append(['OP_BRACK',word])
                elif word == '}':
                    tokens.append(['CL_BRACK',word])
                elif word == '(':
                    tokens.append(['OP_PARENT',word])
                elif word == ')':
                    tokens.append(['CL_PARENT',word])
                elif word == '.':
                    tokens.append(['DOT',word])
                elif word == ',':
                    tokens.append(['COMMA',word])
                elif word ==";":
                    tokens.append(["STATEMENT_END",";"])
                elif word == "(){":
                    tokens.append(['OP_PARENT',word[len(word)-3]])
                    tokens.append(['CL_PARENT',word[len(word)-2]])
                    tokens.append(['OP_BRACK',word[len(word)-1]])
                    
                elif word == "()":
                    tokens.append(['OP_PARENT',word[len(word)-2]])
                    tokens.append(['CL_PARENT',word[len(word)-1]])
                elif word == '"':
                    tokens.append(['QUAT_MARK',word])
                elif word == "'":
                    tokens.append(['PUNC_MARK',word])
                elif word == '>':
                    tokens.append(['GREATER',word])
                elif word == '<':
                    tokens.append(['LESS',word])
                elif word == '!':
                    tokens.append(['NOT',word])
                elif word == '?':
                    tokens.append(['Q_MARK',word])
            else:
                tokens.append(['INVALID',word])
             
            
            
            
    
        #print(tokens)
        #Returnn created tokens
        return tokens
      
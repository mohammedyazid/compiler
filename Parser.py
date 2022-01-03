from enum import Flag
import re
import sys
from compiler import Ui_MainWindow
class Parser(object):
    
    def __init__(self, tokens):
        #This will hold all the tokens that have been created by the lexer
        self.tokens = tokens
        
        #This will hold the token index we are parsing at
        self.token_index = 0
        self.transpiled_code = ""
        
    def parse(self):
        self.line=1
        self.scannerfound = False
        self.classfound = False
        self.mainfound = False
        self.iffound=False
        self.elsefound=False
        self.brackcount=0
        self.opbrackcount=0
        Ui_MainWindow.OUTPUT.setText('')
        while self.token_index<len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]
            
            #######Line Counter#######
            if token_value =='\n': 
                self.line+=1
            if token_type == "CLASS" and token_value == "class" and self.classfound==False:
                tkp = self.tokens[0][0]
                if tkp != "CLASS" and tkp!="NEWLINE":
                    self.DisplayError('nbc')
                else:
                    self.parse_classdeclaration(self.tokens[self.token_index:len(self.tokens)])
                while self.token_index<len(self.tokens):
                    token_type = self.tokens[self.token_index][0]
                    token_value = self.tokens[self.token_index][1]
                    if token_type == "PUBLIC" and token_value == "public" and self.mainfound==False:
                        self.parse_mainfunc(self.tokens[self.token_index:len(self.tokens)])
                    elif token_type == "INT_DECLARATION" and token_value == "int":
                        self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])
                    elif token_type == "CHAR_DECLARATION" and token_value == "char":
                        self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])
                    elif token_type == "FLOAT_DECLARATION" and token_value == "float":
                        self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])
                    elif token_type == "IF_STAT" and token_value == "if":
                        self.parse_ifstatement(self.tokens[self.token_index:len(self.tokens)])
                    elif token_type == "SYSTEM" and token_value == "System" and self.tokens[self.token_index-1][0] == "NEWLINE":
                        self.parse_print(self.tokens[self.token_index:len(self.tokens)])
                    elif token_type == "STRING_DECLARATION" and token_value == "String":
                        self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)]) 
                    elif token_type == "ELSE_STAT" and token_value == "else" and self.iffound==True:
                        self.parse_elsestatement(self.tokens[self.token_index:len(self.tokens)])
                    elif token_type == "SCANNER" and token_value == "Scanner" and self.tokens[self.token_index-1][0] == "NEWLINE":
                        self.parse_scannercheck(self.tokens[self.token_index:len(self.tokens)]) 
                    elif token_type != "PUBLIC" and self.token_index ==len(self.tokens)-1 and self.mainfound==False:
                        Ui_MainWindow.OUTPUT.append(" ERROR : Main Function Not Found")
                    
                        
                    if token_value == "}":
                        self.brackcount+=1      
                    if token_value == "{":
                        self.opbrackcount+=1              
                    self.token_index+=1
                    
                    #######Line Counter#######
                    if token_value =='\n':
                        self.line+=1
                        
            elif token_type != "CLASS" and self.token_index ==len(self.tokens)-1 and self.classfound==False:
                Ui_MainWindow.OUTPUT.append(" ERROR : Class Not Found")
                
            self.token_index+=1
        if self.classfound==True and self.mainfound==True and self.brackcount < 2:
                self.DisplayError('}')
        elif self.classfound==True and self.mainfound==True and self.iffound==False and self.elsefound==False and self.brackcount>2:
            self.DisplayError('+}')
        elif self.iffound==True and self.brackcount<3 and self.elsefound==False:
                self.DisplayError('}')
        elif self.iffound==True and self.brackcount>3 and self.elsefound==False:
            self.DisplayError('+}')
        elif self.iffound==True and self.elsefound==True and self.brackcount<4:
                self.DisplayError('}')
        elif self.iffound==True and self.elsefound==True and self.brackcount>4:
            self.DisplayError('+}')
            
        # if self.classfound==True and self.mainfound==True and self.iffound==False and self.elsefound==False and self.opbrackcount>2:
        #     self.DisplayError('+{')
        # elif self.iffound==True and self.opbrackcount>3 and self.elsefound==False:
        #     self.DisplayError('+{')
        # elif self.iffound==True and self.elsefound==True and self.opbrackcount>4:
        #     self.DisplayError('+{')
        
    ##################Variable Declaration Function############
    def parse_variable_declaration(self,token_stream):
        tokens_checked= 0
        i=0
        for token in range(0,len(token_stream)):
            
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            
            #########Int Declaration###########
            if token_type == "INT_DECLARATION":
                if i < (len(token_stream)-1):
                    i += 1
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_type == "IDENTIF":
                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_value == "=":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                            if token_type == "NUMBER":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if token_type == "STATEMENT_END":
                                    Ui_MainWindow.OUTPUT.append(" Int Declaration success!")
                                    break
                                else:
                                    if token_type == "COMMA" or token_type=="DOT" or token_type=="NUMBER":
                                        self.DisplayError('iva')
                                    else:
                                        self.DisplayError(';')
                            else:
                                if token_type == "IDENTIF":
                                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type=="DOT":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                            if token_type == "NEXT_INT":
                                                if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                                if token_type == "OP_PARENT":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                    if token_type == "CL_PARENT":
                                                        if i < (len(token_stream)-1):
                                                            i += 1
                                                            token_type = token_stream[i][0]
                                                            token_value = token_stream[i][1]
                                                        if token_type == "STATEMENT_END":
                                                            if self.scannerfound ==True:
                                                                Ui_MainWindow.OUTPUT.append(" Getting integer input succesfully!")
                                                                break
                                                            else:
                                                                self.DisplayError('unds')
                                                        else:
                                                            self.DisplayError(';')
                                                    else:
                                                        self.DisplayError(')')
                                                else:
                                                    self.DisplayError('(')
                                            else:
                                                self.DisplayError('nint')
                                        else:
                                            self.DisplayError('.')
                                    else:
                                        self.DisplayError('iva')
                                else:
                                    self.DisplayError('iva')
                        else:
                            if token_value =="STATEMENT_END":
                                Ui_MainWindow.OUTPUT.append(" Int Declaration success!")
                                break
                            elif token_type == "NUMBER" or token_type =="IDENTIF":
                                self.DisplayError(';')
                            else:
                                self.DisplayError('=')
                    else:
                        if token_type == "IDENTIF":
                            self.DisplayError('ivn')
                else:
                    self.DisplayError('ivn')
            ###########Float Declaration################
            if token_type == "FLOAT_DECLARATION":
                i += 1
                token_type = token_stream[i][0]
                token_value = token_stream[i][1]
                if token_type == "IDENTIF":
                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_value == "=":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                            if token_type == "NUMBER":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if token_type == "DOT":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                    if token_type == "NUMBER":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type == "STATEMENT_END":
                                            Ui_MainWindow.OUTPUT.append(" Float Declaration success!")
                                            break
                                        else:
                                            if token_type == "NUMBER" or token_type == "IDENTIF":
                                                self.DisplayError('iva')
                                            else:
                                                self.DisplayError(';')
                                else:
                                    if token_type =="COMMA":
                                        self.DisplayError(',')
                                    elif token_type=="STATEMENT_END":
                                        Ui_MainWindow.OUTPUT.append(" Float Declaration success!")
                                        break 
                            else:
                                if token_type == "IDENTIF":
                                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type=="DOT":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                            if token_type == "NEXT_FLOAT":
                                                if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                                if token_type == "OP_PARENT":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                    if token_type == "CL_PARENT":
                                                        if i < (len(token_stream)-1):
                                                            i += 1
                                                            token_type = token_stream[i][0]
                                                            token_value = token_stream[i][1]
                                                        if token_type == "STATEMENT_END":
                                                            if self.scannerfound ==True:
                                                                Ui_MainWindow.OUTPUT.append(" Getting Float input succesfully!")
                                                                break
                                                            else:
                                                                self.DisplayError('unds')
                                                        else:
                                                            self.DisplayError(';')
                                                    else:
                                                        self.DisplayError(')')
                                                else:
                                                    self.DisplayError('(')
                                            else:
                                                self.DisplayError('nfloat')
                                        else:
                                            self.DisplayError('.')
                                    else:
                                        self.DisplayError('iva')
                                else:
                                    self.DisplayError('iva')
                        
                        else:
                            if token_value =="STATEMENT_END":
                                Ui_MainWindow.OUTPUT.append(" Int Declaration success!")
                                break
                            elif token_type == "NUMBER" or token_type =="IDENTIF":
                                self.DisplayError(';')
                            else:
                                self.DisplayError('=')
                    else:
                        if token_type == "IDENTIF":
                            self.DisplayError('ivn')
                else:
                    self.DisplayError('ivn')
            ############Char Declaration##############
            if token_type == "CHAR_DECLARATION":
                if i < (len(token_stream)-1):
                    i += 1
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_type == "IDENTIF":
                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_value == "=":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                            if token_type == "PUNC_MARK":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if re.match("^[A-Za-z0-9]{1}$",token_value):
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                    if token_type == "PUNC_MARK":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type == "STATEMENT_END":
                                            Ui_MainWindow.OUTPUT.append(" Char Declaration success!")
                                            break
                                        else:
                                            if token_type == "COMMA" or token_type=="DOT" or token_type=="NUMBER":
                                                self.DisplayError('iva')
                                            else:
                                                self.DisplayError(';')
                                    else:
                                        self.DisplayError("'")
                                else:
                                    self.DisplayError('iva')
                            else:
                                self.DisplayError("'")
                        else:
                            self.DisplayError('=')
                    else:
                        self.DisplayError('ivn')
                else:
                    self.DisplayError('ivn')
            
            ##################String Declaration###############
            if token_type == "STRING_DECLARATION":
                i += 1
                token_type = token_stream[i][0]
                token_value = token_stream[i][1]
                if token_type == "IDENTIF":
                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_value == "=":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                            if token_type == "QUAT_MARK":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if re.match("^[A-Za-z0-9]*$",token_value):
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                    if token_type == "QUAT_MARK":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type == "STATEMENT_END":
                                            Ui_MainWindow.OUTPUT.append(" String Declaration success!")
                                            break
                                        else:
                                            if token_type == "COMMA" or token_type=="DOT" or token_type=="NUMBER":
                                                self.DisplayError('iva')
                                            else:
                                                self.DisplayError(';')
                                    else:
                                        self.DisplayError('"')
                                else:
                                    self.DisplayError('iva')
                            else:
                                if token_type == "IDENTIF":
                                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type=="DOT":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                            print(token_type)
                                            if token_type == "NEXT_LINE":
                                                if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                                if token_type == "OP_PARENT":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                    if token_type == "CL_PARENT":
                                                        if i < (len(token_stream)-1):
                                                            i += 1
                                                            token_type = token_stream[i][0]
                                                            token_value = token_stream[i][1]
                                                        if token_type == "STATEMENT_END":
                                                            if self.scannerfound ==True:
                                                                Ui_MainWindow.OUTPUT.append(" Getting Line input succesfully!")
                                                                break
                                                            else:
                                                                self.DisplayError('unds')
                                                        else:
                                                            self.DisplayError(';')
                                                    else:
                                                        self.DisplayError(')')
                                                else:
                                                    self.DisplayError('(')
                                            else:
                                                self.DisplayError('nline')
                                        else:
                                            self.DisplayError('.')
                                    else:
                                        self.DisplayError('iva')
                                else:
                                    self.DisplayError('iva')
                        else:
                            self.DisplayError('=')
                    else:
                        self.DisplayError('ivn')
                else:
                    self.DisplayError('ivn')
                                        
                                           
                     
            tokens_checked+=1
        self.token_index += tokens_checked
    ################Print Function############################
    def parse_print(self,token_stream):
        tokens_checked= 0
        i=0
        for token in range(0,len(token_stream)):
            
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            if token_type == "SYSTEM":
                if i < (len(token_stream)-1):
                    i += 1
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_type == "DOT":
                    if i < (len(token_stream)-1):
                        i += 1
                        token_type = token_stream[i][0]
                        token_value = token_stream[i][1]
                    if token_type == "OUT":
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_type == "DOT":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                            if token_type == "PRINT":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if token_type == "OP_PARENT":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                    if token_type == "QUAT_MARK":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        while token_type != "QUAT_MARK":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                        if token_type == "QUAT_MARK":
                                                if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                                if token_type == "CL_PARENT":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                    if token_type == "STATEMENT_END":
                                                        Ui_MainWindow.OUTPUT.append(" Print Success!")
                                                        break
                                                    else:
                                                        self.DisplayError(';')
                                                else:
                                                    self.DisplayError(')')
                                        else:
                                                self.DisplayError('"')
                                    else:
                                        if token_type == "PUNC_MARK":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                            if re.match("^.{1}$",token_value):
                                                if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                                if token_type == "PUNC_MARK":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                    if token_type == "CL_PARENT":
                                                        if i < (len(token_stream)-1):
                                                            i += 1
                                                            token_type = token_stream[i][0]
                                                            token_value = token_stream[i][1]
                                                        if token_type == "STATEMENT_END":
                                                            Ui_MainWindow.OUTPUT.append(" Print Success!")
                                                            break
                                                        else: 
                                                            self.DisplayError(';')
                                                    else:
                                                        self.DisplayError(')')
                                                else:
                                                    self.DisplayError('"')
                                            else:
                                                self.DisplayError('ivpv')
                                        else:
                                            self.DisplayError('"')
                                else:
                                    self.DisplayError('(')
                            else:
                                self.DisplayError('print')
                        else:
                            self.DisplayError('.')
                    else:
                        self.DisplayError('out')
                else:
                    self.DisplayError('.')
                                            
    ################Check Scanner Declaration#################
    def parse_scannercheck(self,token_stream):
        tokens_checked= 0
        i=0
        
        for token in range(0,len(token_stream)):
            
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            print(token_type)
            if token_type == "SCANNER":
                if i < (len(token_stream)-1):
                    i += 1
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_type == "IDENTIF":
                    if re.match("^[A-Za-z]+[A-Za-z0-9]*$",token_value):
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_type == "OPERATEUR":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]                       
                            if token_type=="NEW":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if token_type == "SCANNER":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                    if token_type == "OP_PARENT":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type=="SYSTEM":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                            if token_type =="DOT":
                                                if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                                if token_type=="IN":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                    if token_type == "CL_PARENT":
                                                        if i < (len(token_stream)-1):
                                                            i += 1
                                                            token_type = token_stream[i][0]
                                                            token_value = token_stream[i][1]
                                                        if token_type == "STATEMENT_END":
                                                            Ui_MainWindow.OUTPUT.append(" scanner declaration success!")
                                                            self.scannerfound =True
                                                            break
                                                        else:
                                                            self.DisplayError(';')
                                                    else:
                                                        self.DisplayError(')')
                                                else:
                                                    self.DisplayError('in')
                                            else:
                                                self.DisplayError('.')
                                        else:
                                            self.DisplayError('system')
                                    else:
                                        self.DisplayError('(')
                                else:
                                    self.DisplayError('scanner')
                            else:
                                self.DisplayError('new')
                        else:
                            self.DisplayError('=')
                    else:
                        self.DisplayError('ivn')
                else:
                    print(token_value)
                    self.DisplayError('ivn')
            if self.scannerfound==True:
                break
            else:
                tokens_checked+=1
                                    
                                                        
    ################CHECK AN INCOMPLETE DECLARATION###########
    def parse_check(self,token_stream):
        tokens_checked= 0
        i=0
        for token in range(0,len(token_stream)):
            
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            if token_type == "IDENTIF":
                if i < (len(token_stream)-1):
                    i += 1
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_value == "=":
                    if i < (len(token_stream)-1):
                        i += 1
                        token_type = token_stream[i][0]
                        token_value = token_stream[i][1]
                    if token_type == "INTEGER" or token_type=="FLOAT":
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_value == ";":
                            self.DisplayError('uvt')
                        else:
                            self.DisplayError(';')
                    else:
                        self.DisplayError('iva')    
                else:
                    if token_value==";":
                        self.DisplayError(';')
                    else:
                        self.DisplayError('=')
            tokens_checked+=1
    ################IF statement Function#############
    def parse_ifstatement(self,token_stream):
        tokens_checked= 0
        i=0
        for token in range(0,len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            if token_type == "IF_STAT":
                if i < (len(token_stream)-1):
                    i += 1
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_type == "OP_PARENT":
                    if i < (len(token_stream)-1):
                        i += 1
                        token_type = token_stream[i][0]
                        token_value = token_stream[i][1]
                    if token_type=="IDENTIF" or token_type=="NUMBER":
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_value ==">" or token_value =="<" or token_value=="=" or token_value=="!":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                            if token_value =="=":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if token_type =="IDENTIF" or "NUMBER":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1] 
                                    if token_type=="CL_PARENT":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        if token_type=="OP_BRACK":
                                            Ui_MainWindow.OUTPUT.append(" If statement success!")
                                            self.iffound=True
                                            break
                                        elif token_type =="NEWLINE":
                                            while token_type =="NEWLINE":
                                                if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                            if token_type!="OP_BRACK":
                                                self.DisplayError('{')
                                            Ui_MainWindow.OUTPUT.append(" If statement success!")
                                            self.iffound=True
                                            break
                                    else:
                                        self.DisplayError(')')
                                else:
                                    self.DisplayError('ivc')
                            else:
                                i = i - 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                                print(token_value)
                                if token_value =="<" or token_value ==">":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                    if token_type =="IDENTIF" or "NUMBER":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1] 
                                        if token_type=="CL_PARENT":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                            if token_type=="OP_BRACK":
                                                Ui_MainWindow.OUTPUT.append(" If statement success!")
                                                self.iffound=True
                                                break
                                            elif token_type =="NEWLINE":
                                                while token_type =="NEWLINE":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                if token_type!="OP_BRACK":
                                                    self.DisplayError('{')
                                                Ui_MainWindow.OUTPUT.append(" If statement success!")
                                                self.iffound=True
                                                break
                                        else:
                                            self.DisplayError(')')
                                    else:
                                        self.DisplayError('ivc')
                                else:
                                    self.DisplayError('<')
                        else:
                            self.DisplayError('<')
                    else:
                        self.DisplayError('ivc')
                else:
                    self.DisplayError('(')
            else:
                self.DisplayError('if')
                
    ##########ELSE Function######################
    def parse_elsestatement(self,token_stream):
        tokens_checked= 0
        i=0
        for token in range(0,len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            if token_type == "ELSE_STAT":
                if i < (len(token_stream)-1):
                    i += 1
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_type=="OP_BRACK":
                    Ui_MainWindow.OUTPUT.append(" else stat success!")
                    self.elsefound=True
                    break
                elif token_type =="NEWLINE":
                    while token_type =="NEWLINE":
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                    if token_type!="OP_BRACK":
                        self.DisplayError('{')
                    Ui_MainWindow.OUTPUT.append(" else stat success!")
                    self.elsefound=True
                    break
            else:
                self.DisplayError('else')
            tokens_checked+=1
    ###################Main Function check############
    def parse_mainfunc(self,token_stream):
        tokens_checked= 0
        i=0
        self.t=False
        for token in range(0,len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            
            token_type = token_stream[i][0]
            token_value = token_stream[i][1]
            if token_type == "PUBLIC":
                if i < (len(token_stream)-1):
                    i += 1            
                    token_type = token_stream[i][0]
                    token_value = token_stream[i][1]
                if token_type == "STATIC":
                    if i < (len(token_stream)-1):
                        i += 1
                        token_type = token_stream[i][0]
                        token_value = token_stream[i][1]
                    if token_type == "VOID":
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        if token_type == "IDENTIF" and token_value=="main":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                            if token_type == "OP_PARENT":
                                if i < (len(token_stream)-1):
                                    i += 1
                                    token_type = token_stream[i][0]
                                    token_value = token_stream[i][1]
                                if token_type == "CL_PARENT":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                        print(token_type)
                                    if token_type == "OP_BRACK":
                                        if i < (len(token_stream)-1):
                                            i += 1
                                            token_type = token_stream[i][0]
                                            token_value = token_stream[i][1]
                                        while token_type == "NEWLINE":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                                self.t=True
                                              
                                        if token_type=="OP_BRACK" and self.t==True:
                                            self.DisplayError("+{")
                                        Ui_MainWindow.OUTPUT.append(" Main success!")
                                        self.mainfound = True
                                        break
                                    elif token_type =="NEWLINE":
                                        while token_type =="NEWLINE":
                                            if i < (len(token_stream)-1):
                                                i += 1
                                                token_type = token_stream[i][0]
                                                token_value = token_stream[i][1]
                                             
                                        if token_type=="OP_BRACK":
                                            if token_type == "NEWLINE":
                                                while token_type =="NEWLINE":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                        self.t=True
                                                       
                                                if token_type=="OP_BRACK" and self.t==True:
                                                    self.DisplayError('+{')
                                            if i < (len(token_stream)-1):
                                                    i += 1
                                                    token_type = token_stream[i][0]
                                                    token_value = token_stream[i][1]
                                            while token_type =="NEWLINE":
                                                    if i < (len(token_stream)-1):
                                                        i += 1
                                                        token_type = token_stream[i][0]
                                                        token_value = token_stream[i][1]
                                                       
                                            if token_type=="OP_BRACK":
                                                self.DisplayError('+{')
                                            Ui_MainWindow.OUTPUT.append(" Main success!")
                                            self.mainfound = True
                                            break
                                        else:
                                            self.DisplayError("{")
                                    else:
                                        self.DisplayError("{")
                                elif token_type !="CL_PARENT":
                                    self.DisplayError(')')
                            elif token_type !="OP_PARENT":
                                self.DisplayError('(')    
                        else:
                            self.DisplayError('f')
                    elif token_type !="VOID":
                        self.DisplayError('void')
                elif token_type !="STATIC":
                    self.DisplayError("stat")
            elif token_type != "PUBLIC":
                    self.DisplayError('pub')
            if self.mainfound==True:
                break
            else:
                tokens_checked+=1
          
        self.token_index += tokens_checked
            
    ###############Class Check######################
    def parse_classdeclaration(self,token_stream):
        tokens_checked= 0
        i=0
        self.t=False
        for token in range(0,len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            if i < (len(token_stream)-1):
                i += 1
                token_type = token_stream[i][0]
                token_value = token_stream[i][1]
            if token_type == "IDENTIF":
                if re.match("^[A-Za-z]+$",token_value):
                    if i < (len(token_stream)-1):
                        i += 1
                        token_type = token_stream[i][0]
                        token_value = token_stream[i][1]
                    if token_type == "OP_BRACK":
                        if i < (len(token_stream)-1):
                            i += 1
                            token_type = token_stream[i][0]
                            token_value = token_stream[i][1]
                        while token_type == "NEWLINE":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                                self.t=True
                        if token_type=="OP_BRACK" and self.t==True:
                            self.DisplayError("+{")
                        Ui_MainWindow.OUTPUT.append(" Class success!")
                        self.classfound = True
                        break
                    elif token_type =="NEWLINE":
                        while token_type =="NEWLINE":
                            if i < (len(token_stream)-1):
                                i += 1
                                token_type = token_stream[i][0]
                                token_value = token_stream[i][1]
                                
                        if token_type=="OP_BRACK":
                            if token_type == "NEWLINE":
                                while token_type =="NEWLINE":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                        self.t=True
                                        
                                if token_type=="OP_BRACK" and self.t==True:
                                    self.DisplayError('+{')
                            if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                            while token_type =="NEWLINE":
                                    if i < (len(token_stream)-1):
                                        i += 1
                                        token_type = token_stream[i][0]
                                        token_value = token_stream[i][1]
                                    
                            if token_type=="OP_BRACK":
                                self.DisplayError('+{')
                            Ui_MainWindow.OUTPUT.append(" Class success!")
                            self.classfound = True
                            break
                        else:
                            
                            self.DisplayError("{")
                    else:
                        self.DisplayError("{")
                elif re.match("^[A-Za-z0-9]+$",token_value):
                    self.DisplayError('ivcn')
            elif token_type != "IDENTIF":
                self.DisplayError('ivcn')
            if self.classfound==True:
                break
            else:
                tokens_checked+=1 
        self.token_index += tokens_checked

    ###########Display Error Message################
    def DisplayError(self,answ):
        if(answ=="("):
            Ui_MainWindow.OUTPUT.append(" ERROR : opened parenthesis expected ' ( ' in line : "+str(self.line))
        if(answ==")"):
            Ui_MainWindow.OUTPUT.append(" ERROR : closed parenthesis expected ' ) ' in line : "+str(self.line))
        if(answ=="{"):
            Ui_MainWindow.OUTPUT.append(" ERROR : opened curly bracket expected ' { ' in line : "+str(self.line))
        if(answ=="}"):
            Ui_MainWindow.OUTPUT.append(" ERROR : closed curly bracket expected ' } ' in line : "+str(self.line))
        if(answ=="+}"):
            Ui_MainWindow.OUTPUT.append(" ERROR : there is an additional curly bracket' } ' in line : "+str(self.line))
        if(answ=="+{"):
            Ui_MainWindow.OUTPUT.append(" ERROR : there is an additional curly bracket' { ' in line : "+str(self.line))
        if(answ=='c'):
            Ui_MainWindow.OUTPUT.append(" SYNTAX ERROR : invalid class name in line : "+str(self.line))
        if(answ=='cnf'):
            Ui_MainWindow.OUTPUT.append(" CLASS NOT FOUND ! ",)
        if(answ=='ivcn'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid class name in line : "+str(self.line))
        if(answ=='pub'):
            Ui_MainWindow.OUTPUT.append(" ERROR : Main fonction not found ( 'public' excpected ) in line : "+str(self.line))
        if(answ=='stat'):
            Ui_MainWindow.OUTPUT.append(" ERROR : Main fonction not found ( 'static' excpected ) in line : "+str(self.line))
        if(answ=='void'):
            Ui_MainWindow.OUTPUT.append(" ERROR : Main fonction not found ( 'void' excpected ) in line : "+str(self.line))
        if(answ=="f"):
            Ui_MainWindow.OUTPUT.append(" SYNTAX ERROR : invalid function name !='main' in line :"+str(self.line))
        if(answ=='iva'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid variable assignement in line : "+str(self.line))
        if(answ=='ivn'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid variable name in line : "+str(self.line) )
        if(answ=='='):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid sentence Operator '=' excpected in line : "+str(self.line))
        if(answ==';'):
            Ui_MainWindow.OUTPUT.append(" ERROR : missing statement end ' ; ' in line : "+str(self.line))
        if(answ=='"'):
            print('ERROR : quotation mark " excpected in line : ',self.line)
        if(answ=="'"):
            Ui_MainWindow.OUTPUT.append(" ERROR : punctuation mark ' excpected in line : "+str(self.line))
        if(answ=='<'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid sentence Operator excpected in line : "+str(self.line))
        if(answ=='ivc'):
            Ui_MainWindow.OUTPUT.append(" ERROR : empty statement or invalid comparison in line : "+str(self.line))
        if(answ=='if'):
            Ui_MainWindow.OUTPUT.append(" ERROR : if statement not found in line : "+str(self.line))
        if(answ=='else'):
            Ui_MainWindow.OUTPUT.append(" ERROR : else statement not found in line : "+str(self.line))
        if(answ=='nbc'):
            Ui_MainWindow.OUTPUT.append(" ERROR : Nothing can be written before class ")
        if(answ=='!s'):
            Ui_MainWindow.OUTPUT.append(" ERROR : the assigned value is not a string value in line : "+str(self.line))
        if(answ=='ndv'):
            Ui_MainWindow.OUTPUT.append(" ERROR : indeclared variable in line : "+str(self.line))
        if(answ=='uvt'):
            Ui_MainWindow.OUTPUT.append(" ERROR : unknown variable type in line : "+str(self.line))
        if(answ=='ivstat'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid statement in line : "+str(self.line))
        if(answ==','):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid character ',' excpected '.' in line : "+str(self.line))
        if(answ=='print'):
            Ui_MainWindow.OUTPUT.append(" ERROR : println expected in line : "+str(self.line))
        if(answ=='out'):
            Ui_MainWindow.OUTPUT.append(" ERROR : incomplete statement 'out' expected in line : "+str(self.line))
        if(answ=='.'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid character excpected dot '.' in line : "+str(self.line))
        if(answ=='new'):
            Ui_MainWindow.OUTPUT.append(" ERROR : incomplete statement 'new' expected in line : "+str(self.line))
        if(answ=='scanner'):
            Ui_MainWindow.OUTPUT.append(" ERROR : incomplete statement 'Scanner' expected in line : "+str(self.line))
        if(answ=='system' or answ =='in'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid scanner statement 'System.in' expected in line : "+str(self.line))
        if(answ=='unds'):
            Ui_MainWindow.OUTPUT.append(" ERROR : undeclared scanner in line : "+str(self.line))
        if(answ=='nint'):
            Ui_MainWindow.OUTPUT.append(" ERROR : excpected nextInt in line : "+str(self.line))
        if(answ=='nfloat'):
            Ui_MainWindow.OUTPUT.append(" ERROR : excpected nextFloat in line : "+str(self.line))
        if(answ=='nline'):
            Ui_MainWindow.OUTPUT.append(" ERROR : excpected nextLine in line : "+str(self.line))
        if(answ=='ivpv'):
            Ui_MainWindow.OUTPUT.append(" ERROR : invalid printed string in line : "+str(self.line))
        if(answ=='unknown'):
            Ui_MainWindow.OUTPUT.append(" ERROR : unknown or invalid statement in line : "+str(self.line))
        raise Stop()
class Stop (Exception):
    def __init__ (self):
        sys.tracebacklimit = 0
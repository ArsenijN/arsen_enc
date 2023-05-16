# -*- coding: utf-8 -*-
import sys

param = sys.argv[1]         # -ne - без конвертування, паролі; -b64 - base64; 
count = int(sys.argv[2])    # кількість
length = int(sys.argv[3])   # довжина
"""
try:
    argument = int(sys.argv[4]) # генерований текст/власний текст (-gen / -user)
except:
    argument = ''
else:
    argument = int(sys.argv[4])


try:
    typetext = int(sys.argv[5]) # (де)кодування (-en / -de)
except:
    typetext = ''
else:
    argument = int(sys.argv[4])
"""
argument = sys.argv[4] # генерований текст/власний текст (-gen / -user)
typetext = sys.argv[5] # (де)кодування (-en / -de)


import random
import base64
import datetime

import re
import unicodedata
chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
#Func-----------------------------------------------------------------------------------
def writefile_base64(fname):
    with open(base64decode, 'w', encoding='utf-8') as f:
        f.writelines(fname)

def writefile(namefile, lines):
    #lines = 'f"{', lines, '}\n"'
    lines = lines, '\n'
    with open(namefile, 'a') as f:
        f.writelines(lines)

def uni_encoding(unicodestring):
    res = (re.sub('.', lambda x: r'\u % 04X' % ord(x.group()), unicodestring))
    unicodestring = res

def uni_encv2(textstr):
    res = (re.sub('.', lambda x: r'\u % 04X' % ord(x.group()), textstr))
    print("Ваш конвертований unicode: " + str(res)) 
    textstr = res
    return(res)

#https://www.google.com/amp/s/www.geeksforgeeks.org/python-convert-string-to-unicode-characters/amp/

def utf8_decode(utfstr):
    utf8decodestr = utfstr.encode('ascii','replace')
    print('decode utf-8: ', utf8decodestr)

def utf8_encode(string):
    utf8encodestr = string.encode('utf-8', 'replace')
    print('utf-8: ', utf8encodestr)

def randomchar(typeoffile):
    if param == "-ne":
        number = count
        #length = input('Їхня довжина: ')
        #number = int(number)
        #length = int(length)
        print('Паролі:')
        if param == "-b64":
            for n in range(number):
                password =''
                for i in range(length):
                    password += random.choice(chars)
                    sample_string = password
                    sample_string_bytes = sample_string.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    base64_string = base64_bytes.decode("ascii")
                print(base64_string)
                writefile(typeoffile, base64_string)
        else:
            for n in range(number):
                password =''
                for i in range(length):
                    password += random.choice(chars)
                print(password)
                writefile(typeoffile, password)

        with open('.temp', 'w') as f:
            f.writelines(typeoffile)

"""
    for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
                if param == '-b64':
                    sample_string = password
                    sample_string_bytes = sample_string.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    outputpasswords = base64_bytes.decode("ascii")
                    password = outputpasswords
            print(password)
            writefile(typeoffile, password)
            
"""
def b64passwords(typeoffile):
    for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
                #if type_encode == '2':
                #sample_string = password
                #sample_string_bytes = sample_string.encode("ascii")
                #base64_bytes = base64.b64encode(sample_string_bytes)
                #outputpasswords = base64_bytes.decode("ascii")
                #password = outputpasswords
            password = password.encode("ascii")
            b64enc = base64.b64encode(password)
            b64enc = b64enc.decode("ascii")
            password = b64enc
            print(password)
            writefile(typeoffile, password)
            with open('.temp', 'w') as f:
                f.writelines(typeoffile)
#dt-------------------------------------------------------------------------------------
dt = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
passtime = 'passwords ' + dt + '.txt'
encgen = 'encrypt.passwords ' + dt + '.txt'
base64decode = 'decode.b64 ' + dt + '.txt'
base64encode = 'encode.b64 ' + dt + '.txt'
#unicode_encode = 'unicode.encode v1 ' + dt + '.txt'
#nameunicode_encodev2 = 'unicode.encode v2' + dt + '.txt'
#unicode_decode = 'unicode_decode ' + dt + '.txt'

if param == "-b64" and argument == "-user" and typetext == "-en":
    unitext = ""
    #print('Введіть власний текст: ')
    from pathlib import Path
    txt = Path('text.temp').read_text()
    #txt = '"' + txt + '"' #'@echo off, ' + '"' + txt + '"'
    #os.system(txt)
    text = txt#open(#"\n".join(iter(input, ""))
    unitext = text.encode(encoding='UTF-8',errors='ignore')
    base64_bytes = base64.b64encode(unitext)
    base64_string = base64_bytes.decode("ascii")
    #print('Ваш зашифрований текст: ', base64_string)
    writefile(base64encode, base64_string)
#    writefile_base64("base64_string")
    with open('.temp', 'w') as f:
        f.writelines(base64encode)

if param == "-b64" and argument == "-user" and typetext == "-de":
    unitext = ""
    #print('Введіть власний текст: ')
    from pathlib import Path
    txt = Path('text.temp').read_text()
    #txt = '"' + txt + '"' #'@echo off, ' + '"' + txt + '"'
    #os.system(txt)
    text = txt#open(#"\n".join(iter(input, ""))
    base64decodetext = text.encode(encoding='UTF-8',errors='ignore')
    base64_bytes = base64.b64decode(base64decodetext)
    base64_string = base64_bytes.decode("ascii")
    #print('Ваш зашифрований текст: ', base64_string)
    writefile(base64decode, base64_string)
#    writefile_base64("base64_string")
    with open('.temp', 'w') as f:
        f.writelines(base64decode)

#

#
if param == "-ne":
    number = count
    #length = int(input('Їхня довжина: '))
    print('Паролі:')
#    if param == '-b64':
#        randomchar(encgen)
#    else:
    randomchar(passtime)

if param == '-b64' and argument == '' and typetext == '':
    number = count
    #length = int(input('Їхня довжина: '))
    print('Паролі:')
    b64passwords(encgen)




"""
if param == "-b64" and argument == "-user" and typetext == "-de":
    encrypt_usertext = input('Введіть зашифрований текст: ')
    base64_string = base64.b64decode(encrypt_usertext)
    base64_bytes = base64_string.decode()
    print("Декодована строка: ", base64_bytes)
    writefile(base64decode, base64_bytes)
    with open('.temp', 'w') as f:
        f.writelines(typeoffile)

"""

#with open('.temp', 'a') as f:
#        f.writelines(bbtx)
#pause
#writefile('.data', typeoffile)
"""
if type_text == "1":
    number = int(input('Кількість паролів: '))
    length = int(input('Їхня довжина: '))
    print('Паролі:')
    if type_encode == "2":
        randomchar(encgen)
    else:
        randomchar(passtime)
"""

"""
Комментар?
Змінено параметри використовуваних символів, а саме додано маленьку літеру m
"""

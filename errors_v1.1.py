#!/usr/bin/envi python3

import os, sys

path = os.path.join(os.curdir, "files")
filepath = os.path.join(path, "names.txt")

# EAFP - Easy to Ask Forgiveness than Permission
try:
    names = open(filepath).readlines() #FileNotFoundError
    #1 / 0 #ZeroDivisionError
    #print(names.banana) #AttributeError
except FileNotFoundError as error:
    print(f"{str(error)}")
    sys.exit(1)
    # TODO: use retry
# except ZeroDivisionError: 
#     print("[Error] You can't divide by zero")
#     sys.exit(1)
# except AttributeError:
#     print("[Error] List doesn't have banana")
#     sys.exit(1)
# except: #Bare except
#     print("[Error] Unknown error")
else: # executado quando o try ocorre com sucesso
    print("Sucesso") 
finally: # sempre executado, independente se deu erro ou não 
    print("Execute isso sempre")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
#!/usr/bin/envi python3

import os, sys, logging, time

log = logging.Logger("errors")

path = os.path.join(os.curdir, "files")
filepath = os.path.join(path, "names.txt")

# Retry com loop
def try_to_open_a_file_loop(filepath, retry=1):
    for attempt in range(0, retry):
        # EAFP - Easy to Ask Forgiveness than Permission
        try:
            return open(filepath).readlines() #FileNotFoundError
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
            time.sleep(1)
        # except: #Bare except
        #     print("[Error] Unknown error")
        else: # executado quando o try ocorre com sucesso
            print("Sucesso") 
        finally: # sempre executado, independente se deu erro ou não 
            print("Retry com loop\n")
    return []

# Retry com recursao
def try_to_open_a_file_recursao(filepath, retry=1):
    if retry > 999:
        raise ValueError("Retrt cannot be more then 999 because of Python recursion limits")
        
    # EAFP - Easy to Ask Forgiveness than Permission
    try:
        return open(filepath).readlines() #FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(1)
        if retry > 1:
            # recursao 
            return try_to_open_a_file_recursao(filepath, retry=retry - 1)
    # except: #Bare except
    #     print("[Error] Unknown error")
    else: # executado quando o try ocorre com sucesso
        print("Sucesso") 
    finally: # sempre executado, independente se deu erro ou não 
        print("Retry com recursao\n")
    return []

for line in try_to_open_a_file_loop(filepath, retry=5):
    print(line)

for line in try_to_open_a_file_recursao(filepath, retry=5):
    print(line)

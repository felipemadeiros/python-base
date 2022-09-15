#!/usr/bin/env python3
"""Bloco de notas

Usage:
$ notes.py new "Minha nota"
tag: tech
text:
Algum texto aqui

$ notes.py read {tag}
...
...
"""

__version__ = "0.1.0"

import os
import sys

path = os.path.join(os.curdir, "files")
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")
arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 50)
            print()

if arguments[0] == "new":
    try:
        titulo = arguments[1]
    except IndexError as error:
        # TODO: logging
        print(f"[Error] {error}")
        print("Informe um titulo para sua anotacao")
        print("e.g: notes.py new 'SOME TITLE'")
        sys.exit(1)
    text = [
        f"{titulo}",
        input("tag: ").strip(),
        input("text: ").strip()
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

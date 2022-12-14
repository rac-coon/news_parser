# -*- coding: utf-8 -*-
import os

if __name__ == "__main__":
    names = ["S", "M", "L"]
    for i in range(0, 3):
        os.chdir(names[i])
        text = ("URL\n07.04.2022\nКол-во слов\nКол-во символов\n7\nДоп темы")
        for j in range(1, 300):
            # text_file = open(i + ".txt", "w")
            # text_file.write(text)
            # text_file = open(i + ".docx", "w")
            with open(str(j) + ".docx", "w", encoding="utf-8") as file:
                file.write("")
            with open(str(j) + ".txt", "w", encoding="utf-8") as file:
                file.write(text)

import os
import sys
from time import sleep
import colorama


class Diy:
    def __init__(self, fg=colorama.Fore.BLUE, end=" ", time_between_interval=0.3):
        self.fg = fg
        self.time_between_interval = time_between_interval
        self.end = end

    def word(self, word: str):
        for i in range(len(word)):
            print(self.fg + word[i], end=self.end, flush=True);
            sleep(self.time_between_interval)

    def pattern(self, char: str, num=10):
        for i in range(num):
            print(self.fg + char, end=self.end, flush=True);
            sleep(self.time_between_interval)

    def inter(self, pattern: list, num=10):
        while num:
            num = num - 1
            for x in pattern:
                sleep(0.3)
                print(str(x) + '\r', end="")

    def msf(self, sentence: str, time: int):
        load_str = sentence
        ls_len = len(load_str)

        animation = "|/-\\"
        anicount = 0

        counttime = 0

        i = 0

        while counttime != time:

            sleep(0.075)

            load_str_list = list(load_str)

            x = ord(load_str_list[i])

            y = 0

            if x != 32 and x != 46:
                if x > 90:
                    y = x - 32
                else:
                    y = x + 32
                load_str_list[i] = chr(y)

            res = ''
            for j in range(ls_len):
                res = res + load_str_list[j]

            sys.stdout.write("\r" + res + animation[anicount])
            sys.stdout.flush()

            load_str = res

            anicount = (anicount + 1) % 4
            i = (i + 1) % ls_len
            counttime = counttime + 1

        if os.name == "nt":
            os.system("cls")

        else:
            os.system("clear")


class Prebuild:
    def __init__(self, fg=colorama.Fore.BLUE, end=" ", time_between_interval=0.3):
        self.fg = fg
        self.time_between_interval = time_between_interval
        self.end = end

    def printProgressBar(self, fill='█', num=10):
        for i in range(num):
            print(self.fg + fill, end=" ", flush=True);
            sleep(self.time_between_interval)

    def num(self, num=10):
        for i in range(num):
            print(self.fg + str(i) + '\r', end="")
            sleep(0.1)

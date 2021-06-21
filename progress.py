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
            sleep(time_between_interval)

    def inter(self, pattern: list, num=10):
        while num:
            num = num - 1
            for x in pattern:
                sleep(0.3)
                print(str(x) + '\r', end="")


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


Diy().inter(["/", "|", "\\"])

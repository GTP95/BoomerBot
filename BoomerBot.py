# Simple boomer bot.
import random
import time

import pydle


def count_quotes(filepath):
    count = 0
    with open(filepath) as fp:
        for line in fp:
            if line.strip():
                count += 1
    return count


class BoomerBot(pydle.Client):
    distroList = '''\
    Ecco un elenco delle distribuzioni Linux che puoi scaricare:
    1. Arch Linux
    2. Fedora
    3. Rocky Linux
    4. Ubuntu\
    '''

    arch = '''\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⣤⣙⢻⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡿⠛⠛⠿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⠿⣆⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀
⠀⢀⣾⣿⣿⠿⠟⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠻⠿⣿⣿⣷⡀⠀
⣠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣄\
    '''

    ubuntu = '''\
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣦⠀⠀⠀⠈⢻⣿⣿⣿
⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣾⣷⣶⣆⠸⣿⣿⡟⠀⠀⠀⠀⠀⠹⣿⣿
⣿⠃⠀⠀⠀⠀⠀⠀⣠⣾⣷⡈⠻⠿⠟⠻⠿⢿⣷⣤⣤⣄⠀⠀⠀⠀⠀⠀⠘⣿
⡏⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⠀⠀⠀⠀⠀⠀⢹
⠁⠀⠀⢀⣤⣤⡘⢿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⠀⠀⠀⠈
⠀⠀⠀⣿⣿⣿⡇⢸⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣉⣉⡁⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠈⠛⠛⢡⣾⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⢀
⣇⠀⠀⠀⠀⠀⠀⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠀⠀⠀⠀⠀⠀⣸
⣿⡄⠀⠀⠀⠀⠀⠀⠙⢿⡿⢁⣴⣶⣦⣴⣶⣾⡿⠛⠛⠋⠀⠀⠀⠀⠀⠀⢠⣿
⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⢿⡿⠿⠏⢰⣿⣿⣧⠀⠀⠀⠀⠀⣰⣿⣿
⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⠟⠀⠀⠀⢀⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿\
'''

    fedora_braille = '''\
⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⢠⢢⢪⢪⢪⢪⢪⢢⢢⢢⢠⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡀⡔⡜⡜⡜⡜⡜⡜⡔⡕⡕⡱⡱⡱⡑⡕⡅⡇⡆⡄⠀⠀⠀⠀⠀
⠀⠀⠀⡀⡆⡇⡇⢇⢇⢇⢇⢇⢣⢣⠣⡣⡣⡣⡪⡪⡪⡪⡪⡪⡪⡢⢄⠀⠀⠀
⠀⠀⡰⡸⡸⡨⡪⡪⡪⡢⡣⡣⡣⡣⡣⠃⠁⠀⠀⠈⠈⠪⡢⡣⡪⡪⡪⡢⠀⠀
⠀⡰⡱⡑⡕⡕⢕⢕⠕⡕⢕⢕⢜⠌⠀⠀⢠⢰⢐⢄⠀⠀⠑⢕⢕⢕⢕⢜⠤⠀
⢐⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⢜⠄⠀⠀⢕⢕⢕⢕⠅⠀⠀⢕⢕⢅⢇⢇⢝⠄
⡪⡪⡪⡢⡣⡣⡱⣑⢅⢇⢇⢕⢕⠅⠀⠀⢕⢕⢕⢕⢱⢰⢸⢸⢸⠸⡸⡘⡜⡔
⢣⢣⢪⢪⠪⡪⡪⠢⠃⠁⠁⠁⢱⠁⠀⠀⠁⠁⠁⢣⢣⠣⡣⡱⡱⡱⡱⡱⡱⡱
⡱⡑⡕⢕⢕⠕⠀⠀⢀⢠⢠⢠⢜⠂⠀⠀⢄⢄⢄⢕⢕⢕⢕⢕⢕⢕⢱⢑⢕⠜
⢕⢕⢕⢕⢕⠀⠀⢠⢣⠣⡣⡣⢣⠃⠀⠀⢕⢕⢕⢕⢕⢕⢱⢑⢅⢇⢇⢇⢇⠇
⢕⢕⠕⡕⡅⠀⠀⢘⢜⢜⢜⢜⢜⠂⠀⠠⡱⡱⡱⡑⡅⡇⡇⡇⡇⡇⡇⡣⠕⠀
⢕⢕⢕⢕⢕⡂⠀⠀⠁⠃⠕⠑⠁⠀⠀⡜⡜⡜⢜⢜⢜⢜⢜⠜⡜⡌⡎⠎⠀⠀
⢕⢕⢕⢱⢱⢸⢑⢄⡀⡀⢀⢀⢀⢄⢇⢇⢇⢎⢎⢎⢎⢪⢢⢣⢣⠣⠃⠀⠀⠀
⢕⢕⢕⢕⢕⠕⡕⡕⡜⡜⡜⡜⡜⡜⡜⡜⢜⢜⢜⢜⢜⢜⢜⠜⠈⠀⠀⠀⠀⠀
⠈⠪⢢⢣⢱⢱⢱⢱⠱⡱⡱⡑⡕⢕⢕⢜⢜⢜⠔⠕⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀\
'''
    rocky_braille = '''\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⡄⡄⡄⡄⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡄⡆⡇⡇⡇⡇⡇⡇⡇⡇⡇⡏⠦⡄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡔⡕⡕⡕⡕⡕⡕⡕⡕⡕⡕⡕⡕⡍⡇⡇⡗⡢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⠆⠀⠀⠀⠀
⠀⠀⠀⢀⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⢇⠇⢇⢇⢇⢇⢇⢇⢏⠄⠀⠀⠀
⠀⠀⠀⢔⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⠕⠁⠀⠈⠊⡎⡎⡎⡎⡎⡖⠀⠀⠀
⠀⠀⠀⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⠕⠁⠀⠀⠀⠀⠀⠈⠸⡸⡸⡸⡸⠀⠀⠀
⠀⠀⠀⢕⢕⢕⢕⢕⢕⢕⢕⢕⠕⠁⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠃⡇⡗⠀⠀⠀
⠀⠀⠀⠐⢕⢕⢕⢕⢕⢕⠕⠁⠀⠀⠀⠀⢠⢸⢸⢰⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠀⠑⢕⢕⢕⠕⠁⠀⠀⠀⠀⡀⡜⡜⡜⡜⡢⡣⡣⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠊⠀⠀⠀⠀⠀⡀⡆⡇⡇⡇⡇⡇⡇⡇⡇⡇⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡆⡇⡇⡇⡇⡇⡇⡇⡇⡇⠇⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠑⠑⠑⠑⠑⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\
'''

    l='''\
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣤⣤⣀⣀⣀⣀⣠⠄⢀⣀⣤⠤⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⡿⠿⣿⣿⣿⣿⠿⣿⡟⠁⣴⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠃⠄⠄⠄⠄⠄⢀⣾⡟⠄⢰⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿⡇⠄⢸⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⡇⠄⢸⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣸⣿⣿⣧⠄⢸⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠚⠛⠻⣿⣿⣿⣿⠄⢸⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿⡿⠄⢸⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠛⢿⣿⣿⡇⠄⣼⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⡿⠄⣰⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡿⣡⣾⣫⣤⣶⣶⣶⣶⣦⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣶⠞⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠴⠞⠋⠉⠄⠄⠄⠄⠄⠄⠄⠉⠙⠿⣿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
'''

    def __init__(self, nickname, realname, listOfChannels):
        pydle.Client.__init__(self, nickname, fallback_nicknames=[], username=None, realname=realname, eventloop=None)
        self.listOfChannels = listOfChannels
        self.numOfQuotes = count_quotes("quotes.txt")
        self.lastAnsaCall=0
        self.nickname=nickname

    async def on_connect(self):
        for channel in self.listOfChannels:
            await self.join(channel)

    async def ansa(self, target):
        now=int(time.time())
        if now-self.lastAnsaCall>=30:
            await self.message(target, "Ansa, che ansia!")
            self.lastAnsaCall=now


    async def on_message(self, target, source, message):
        # don't respond to our own messages, as this leads to a positive feedback loop
        if source != self.nickname:
            if "E' mezzanotte! Un nuovo giorno e' alle porte! Oggi e'" in message and source == "[KIRA]":
                randomInt = random.randrange(5)
                # Since I'm not on Python 3.10, I can't use match/case.
                # Really, Python? Wait until 3.10 for a switch/case?
                answers = {
                    0: "Buongiornissimo, caffè?",
                    1: "[KIRA], ma quanto sei boomer?",
                    2: "https://www.youtube.com/watch?v=-NuptTvNSJY",
                    3: "https://www.youtube.com/watch?v=qR6dzwQahOM",
                    4: "https://www.youtube.com/watch?v=ZXmEgIERQBo"
                }
                await self.message(target, answers[randomInt])
            elif "[Ansa Tecnologia]" in message:
                await self.ansa(target)
            elif message == "!list":
                await self.message(target, self.distroList)
            elif message == "!1":
                await self.message(target, "Ottima scelta!")
                await self.message(target, self.arch)
            elif message == "!2":
                await self.message(target, self.fedora_braille)
            elif message == "!3":
                await self.message(target, self.rocky_braille)
            elif message == "!4":
                await self.message(target, self.ubuntu)
            elif message == "!help":
                await self.message(target, "Ti posso aiutare per la modica cifra di 50€, pagamento anticipato")
            elif self.nickname.lower() in message.lower() and "chi" and "sei" in message.lower():
                await self.message(target, self.l)
            elif self.nickname.lower() in message.lower():
                quoteIndex = random.randrange(self.numOfQuotes)
                currentLine = 0
                file = open("quotes.txt", "r")
                for line in file:
                    if currentLine == quoteIndex:
                        await self.message(target, line.strip('\n'))
                        break
                    currentLine += 1

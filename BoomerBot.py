# Simple boomer bot.
import pydle


class BoomerBot(pydle.Client):
    distroList = '''
    Ecco un elenco delle distribuzioni Linux che puoi scaricare:
    1. Arch Linux
    2. Fedora
    3. Rocky Linux
    4. Ubuntu
    '''

    def __init__(self, nickname, realname, listOfChannels):
        pydle.Client.__init__(self, nickname, fallback_nicknames=[], username=None, realname=realname, eventloop=None)
        self.listOfChannels = listOfChannels

    async def on_connect(self):
        for channel in self.listOfChannels:
            await self.join(channel)

    async def on_message(self, target, source, message):
        # don't respond to our own messages, as this leads to a positive feedback loop
        if source != self.nickname:
            if "E' mezzanotte! Un nuovo giorno e' alle porte! Oggi e'" in message:
                await self.message(target, "Buongiornissimo, caffè?")
            elif message=="!list":
                await self.message(target, self.distroList)


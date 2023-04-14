# Simple boomer bot.
import pydle


class BoomerBot(pydle.Client):
    async def on_connect(self):
        await self.join('#bottest')

    async def on_message(self, target, source, message):
        # don't respond to our own messages, as this leads to a positive feedback loop
        if source != self.nickname:
            if "E' mezzanotte! Un nuovo giorno e' alle porte! Oggi e'" in message:
                await self.message(target, "Buongiornissimo, caffè?")

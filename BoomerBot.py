# Simple boomer bot.
import pydle
import threading


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
    fedora = '''\
       ,\'\'\'\'\'.
       |   ,.  |
       |  |  '_'
  ,....|  |..
.'  ,_;|   ..'
|  |   |  |
|  ',_,'  |
 '.     ,'
   \'\'\'\'\'\
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

    rocky = '''\
         __wgliliiligw_,
       _williiiiiiliilililw,
     _%iiiiiilililiiiiiiiiiii_
   .Qliiiililiiiiiiililililiilm.
  _iiiiiliiiiiililiiiiiiiiiiliil,
 .lililiiilililiiiilililililiiiii,
_liiiiiiliiiiiiiliiiiiF{iiiiiilili,
jliililiiilililiiili@`  ~ililiiiiiL
iiiliiiiliiiiiiili>`      ~liililii
liliiiliiilililii`         -9liiiil
iiiiiliiliiiiii~             "4lili
4ililiiiiilil~|      -w,       )4lf
-liiiiililiF'       _liig,       )'
 )iiiliii@`       _QIililig,
  )iiii>`       .Qliliiiililw
   )<>~       .mliiiiiliiiiiil,
            _gllilililiililii~
           giliiiiiiiiiiiiT`
          -^~$ililili@~~'\
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

    def __init__(self, nickname, realname, listOfChannels):
        pydle.Client.__init__(self, nickname, fallback_nicknames=[], username=None, realname=realname, eventloop=None)
        self.listOfChannels = listOfChannels

    async def on_connect(self):
        for channel in self.listOfChannels:
            await self.join(channel)

    async def ansa(self, target):
        await self.message(target, "Ansa, che ansia!")

    async def on_message(self, target, source, message):
        # don't respond to our own messages, as this leads to a positive feedback loop
        if source != self.nickname:
            if "E' mezzanotte! Un nuovo giorno e' alle porte! Oggi e'" in message:
                await self.message(target, "Buongiornissimo, caffè?")
            elif "[Ansa Tecnologia]" in message:
                timer=threading.Timer(30.0, self.ansa(target))
                timer.start()
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

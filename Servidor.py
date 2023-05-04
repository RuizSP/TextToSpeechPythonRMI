import Pyro4
import os
from gtts import gTTS

@Pyro4.expose

class StreamServer (object):
    def textReceiver(self, texto):
        tts = gTTS(texto, lang = 'pt-br')
        tts.save("audioInfo.mp3")
        os.system("mpg321 audioInfo.mp3")
        os.system('mplayer audioInfo.mp3')


def main():
    Pyro4.Daemon.serveSimple({
        StreamServer: "servidor.Fala"
    })
if __name__ == "__main__":
    main()

#fazer rodar em maquinas diferentes
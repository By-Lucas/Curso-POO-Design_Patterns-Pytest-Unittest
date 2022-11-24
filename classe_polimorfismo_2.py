

class AudioFile:

    def __init__(self, filename):
        
        # A classe (__init__) pai consegue saber o tipo de arquivo
        # usando polimorfismo
        if not filename.endswith(self.ext):
            raise Exception('Audio não encontrado')
        
        self.filename = filename


class MP3File(AudioFile):

    ext = 'mp3'

    def play(self):
        print('Tocando arquivo mp3')


class WavFile(AudioFile):

    ext = 'wav'

    def play(self):
        print('Tocando arquivo wav')


class OggFile(AudioFile):

    ext = 'ogg'

    def play(self):
        self.ext = 'ogg'
        print('Tocando arquivo ogg')


# Formato correto de reproducao
mp3 = MP3File('musica.mp3')
mp3.play()
wav = WavFile('musica.wav')
wav.play()
ogg = OggFile('musica.ogg')
ogg.play()

# Mostrando o erro quando não encontra o formato correto dentro da classe
mp3 = MP3File('musica.wav')
mp3.play()
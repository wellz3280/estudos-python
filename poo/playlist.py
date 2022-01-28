
class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas

    # transforma em interavel
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __add__(self, other):
        return Playlist(self._programas + other)

     # metodo magico
    def __len__(self):
        return len(self._programas)

from filme import Filme
from serie import Serie
from playlist import Playlist
from abc import ABC


vingadores = Filme('Vingadores a era de ultron',2015,160)
vingadores.dar_like()

atlanta = Serie('atlanta',2018,2)
atlanta.dar_like()
atlanta.dar_like()

tmep = Filme('todo mundo em panico',2008,90)
tmep.dar_like()

fringe = Serie('fringe',2013,4)
fringe.dar_like()
fringe.dar_like()
fringe.dar_like()

filmes_e_saries= [vingadores,atlanta,tmep,fringe]

playlist_passa_tempo = Playlist('passa tempo',filmes_e_saries)
print(f'{playlist_passa_tempo.nome} com {len(playlist_passa_tempo)} programas')

for programa in playlist_passa_tempo:
    print(programa)

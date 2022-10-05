"""import vlc
print('{:=^31}'.format('Exercício 021'))
m = "Music.mp3"
a = vlc.MediaPlayer(m)
a.play()
print('Musica em reprodução: Turn The Page - Metallica')
input('Stop (Press Enter)') - Forma feita inicialmente utilizando o modulo vlc"""
import playsound
playsound.playsound('Music.mp3')


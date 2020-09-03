import sys 
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt 
seno =SinSignal(freq=440, amp=1, offset=0)
segundo_seno= SinSignal(freq=340, amp=0.7, offset=0)
tercer_seno= SinSignal(freq=600, amp=0.4, offset=0)

wave_seno = seno.make_wave(duration=1.0,start=0,framerate=44100)
wave_segundo_seno = segundo_seno.make_wave(duration=1.0,start=1,framerate=44100)
wave_tercer_seno = tercer_seno.make_wave(duration=1.0,start=2,framerate=44100)

resultante= wave_seno + wave_segundo_seno + wave_tercer_seno

decorate(xlabel='Tiempo(s)')
decorate(ylabel='Amplitud')
wave_seno.plot()
resultante.plot()
wave_seno.write("sonido.wav")
plt.show()
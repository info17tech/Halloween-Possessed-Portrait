dl302@soetcse:~$ cd bhavna
dl302@soetcse:~/bhavna$ pip3 install pyaudio
Collecting pyaudio
Installing collected packages: pyaudio
Successfully installed pyaudio-0.2.11
dl302@soetcse:~/bhavna$ pip3 install SpeechRecognition
Collecting SpeechRecognition
  Using cached https://files.pythonhosted.org/packages/26/e1/7f5678cd94ec1234269d23756dbdaa4c8cfaed973412f88ae8adf7893a50/SpeechRecognition-3.8.1-py2.py3-none-any.whl
Installing collected packages: SpeechRecognition
Successfully installed SpeechRecognition-3.8.1
dl302@soetcse:~/bhavna$ arecord mifi.py
Recording WAVE 'mifi.py' : Unsigned 8 bit, Rate 8000 Hz, Mono

^Z
[1]+  Stopped                 arecord mifi.py
dl302@soetcse:~/bhavna$ python3 mifi.py 
  File "mifi.py", line 1
SyntaxError: Non-UTF-8 code starting with '\xfb' in file mifi.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
dl302@soetcse:~/bhavna$ arecord example2.way
Recording WAVE 'example2.way' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[2]+  Stopped                 arecord example2.way
dl302@soetcse:~/bhavna$ python3 mifi.py 
  File "mifi.py", line 1
SyntaxError: Non-UTF-8 code starting with '\xfb' in file mifi.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[3]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:afternoon
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[4]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:3rd class
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[5]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:HSC afternoon
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[6]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:hey afternoon
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[7]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:full episode today afternoon
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[8]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:Essentials salon
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[9]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:Thursday afternoon
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[10]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:afternoon
dl302@soetcse:~/bhavna$ arecord example2.wav
Recording WAVE 'example2.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono
^Z
[11]+  Stopped                 arecord example2.wav
dl302@soetcse:~/bhavna$ python3 microfle.py
The audio file contains:ok afternoon
dl302@soetcse:~/bhavna$ python3 microd.py
  File "microd.py", line 16
    except sr.UnknownValueError
                              ^
SyntaxError: invalid syntax
dl302@soetcse:~/bhavna$ python3 microd.py
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
Traceback (most recent call last):
  File "microd.py", line 5, in <module>
    r,adjust_for_ambient_noise(source,duration=5)
NameError: name 'adjust_for_ambient_noise' is not defined
dl302@soetcse:~/bhavna$ python3 microd.py
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
Traceback (most recent call last):
  File "microd.py", line 5, in <module>
    r,adjust_for_ambient_noise(source,duration=5)
NameError: name 'adjust_for_ambient_noise' is not defined
dl302@soetcse:~/bhavna$ python3 microd.py
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
Say Something!
you said: + r.recognize_google(audio)
dl302@soetcse:~/bhavna$ python3 microd.py
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
Say Something!
you said: + r.recognize_google(audio)
dl302@soetcse:~/bhavna$ python3 microd.py
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
Say Something!
you said: hey sorry sorry
dl302@soetcse:~/bhavna$ 


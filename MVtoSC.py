
import os
import subprocess
import speech_recognition as sr

f = open('DD基礎1.txt', 'a',encoding='UTF-8')


start = 0
cut = 20
finish = 10

min_start = 0
h_start = 0
min_cut = 0
h_cut = 0
file_dd = "/Users/shibusawasatoshi/info2/DD基礎1.mp4"
text='データ・ドリブン 第一回'
while min_start <= finish:
    file_cut = "DD_1_1.mp4"
    file_wav = "DD_1_1.wav"
    print(  str(h_start) + ':'+ str(min_start) + ':'+ str(start) )
    print(str(h_cut) + ':'+ str(min_cut) + ':'+ str(cut) )
    cmd = 'ffmpeg -ss ' + str(h_start) + ':'+ str(min_start) + ':'+ str(start) + ' -t 0:0:20  -i ' + file_dd + ' -vcodec copy -acodec copy ' + file_cut + ' -y'
    cmd2 = 'ffmpeg -i ' +file_cut+ ' -f wav -ab 192000 -vn ' +file_wav
    subprocess.call(cmd.split())
    subprocess.call(cmd2.split())

    file_where_wav = os.path.abspath(file_wav)
    file_where_cut = os.path.abspath(file_cut)
    print(file_where_wav)

    r = sr.Recognizer()
    with sr.AudioFile(file_where_wav) as source:
        audio = r.record(source)
    text =  r.recognize_google(audio, language='ja-JP')
    f.write(text)

    start = start + 20
   # cut = cut +20
    if cut >= 60:
        cut -= 60
        min_cut += 1
    if min_cut >= 60:
        min_cut -= 60
        h_cut += 1
    if start >= 60:
        start -= 60
        min_start += 1
    if min_start >= 60:
        min_start -= 60
        h_start += 1
    print(text)
    os.remove(file_where_wav)
    os.remove(file_where_cut)


print(text)







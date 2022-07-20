from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

filename = askopenfilename(title='Target File')
filesave= asksaveasfilename(title='Save As')


print('Enter AudioCodec Type')
audiocodec = input()
print('Enter LFE Middle Filter Frequency')
hfreq = input()
print('Enter Frequency Filter Width')
freqwidth = input()
print('Enter LFE Gain')
lfegain = input()

import subprocess

ffmpegloc = r'C:\ffmpeg\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe'
bassoptions= '-af bass=f='+ hfreq +',bass=g='+ lfegain +',bass=c=LFE,bass=w='+ freqwidth +''


output = f'"{ffmpegloc}" -i "{filename}" -c:v copy -c:a "{audiocodec}" {bassoptions} "{filesave}"'
output1 = f'"{ffmpegloc}" -i "{filename}" -c:v copy -c:a "{audiocodec}" -strict -2 {bassoptions} "{filesave}"'
print(audiocodec)

if audiocodec in ['truehd','dts']:
    subprocess.run(output1)
    print('Experimental Enabled')
    print(output1)
else:
    subprocess.run(output)
    print('Normal Run')
    print(output)






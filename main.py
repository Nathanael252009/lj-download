from gtts import gTTS
inport os

msg = 'Has sido hackeando'
language ='en'

obj=gTTs(text=msg, lang=language, slow=False)

obj.save('Virus.mp4')

os.system('mpg321 Virus.mp4')

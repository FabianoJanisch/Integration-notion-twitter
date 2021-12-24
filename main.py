import tweepy
import time
from PIL import Image, ImageDraw, ImageFont
from DownloadImage import DownloadImage
from RandomizePhrase import RandomizePhrase
import textwrap
from string import ascii_letters

API_KEY = '8TtCsXN7WOzWX9hEMQWIoXAZq'
API_SKEY = 'h0Azcyi6Tpv7Nqi9WofEcVZnuLgvLbIXWsMcMrvZ7tnYyUA5Gf'
ACESS_KEY = '1275783034311266306-klktQvxULS3mHuhHsPWJ1Ghg2oCF9Y'
ACESS_SKEY = 'lweAKtZEitTIlBXnLy3rndNJYfq0RKTIfwXvZmsILj1SK'

auth = tweepy.OAuthHandler(API_KEY, API_SKEY)
auth.set_access_token(ACESS_KEY, ACESS_SKEY)
api = tweepy.API(auth)

while True:
    time.sleep(25)
    hora = time.gmtime()
    if hora[3] == 10 and hora[4] == 00:
        ImageO = DownloadImage()
        imageline = Image.open('IMGDownload.png')
        Cont = RandomizePhrase()
        listatexto = Cont[0]
        
        textorandomR = listatexto.replace ('.', '')
        textorandom2 = listatexto.split()
        textorandom3 = ' '.join(textorandom2)

        imageline = imageline.resize((1080, 1080))
        color = (255, 255, 255)
        font = ImageFont.truetype(f'{Cont[1]}.ttf', Cont[2])

        avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
        max_char_count = int(imageline.size[0] / avg_char_width)
        text2 = textwrap.fill(text=listatexto, width=max_char_count)

        drawline = ImageDraw.Draw(imageline)
        drawline.text(xy=(imageline.size[0]/2, 100), text=text2,fill=(color), font=font, anchor='ms')

        imageline.save('amigotimeline.png')
        api.update_status_with_media (textorandom3, 'amigotimeline.png')
        imageline.close()
        print ("(Tweet enviado na timeline)")
        time.sleep(82.800)

import tweepy
import time
import random
from PIL import Image, ImageDraw, ImageFont

API_KEY = '8TtCsXN7WOzWX9hEMQWIoXAZq'
API_SKEY = 'h0Azcyi6Tpv7Nqi9WofEcVZnuLgvLbIXWsMcMrvZ7tnYyUA5Gf'
ACESS_KEY = '1275783034311266306-klktQvxULS3mHuhHsPWJ1Ghg2oCF9Y'
ACESS_SKEY = 'lweAKtZEitTIlBXnLy3rndNJYfq0RKTIfwXvZmsILj1SK'

auth = tweepy.OAuthHandler(API_KEY, API_SKEY)
auth.set_access_token(ACESS_KEY, ACESS_SKEY)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

while True:
    time.sleep(25)
    hora = time.gmtime()
    if hora[3] == 10 and hora[4] == 00:
        listatimeline = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.jpg', '7.jpeg', '8.png', '9.png', '10.png', '11.jpeg', 
        '12.png', '13.png', '14.png', '15.png', '16.png', '17.png']
        fotoline = random.choice(listatimeline)
        imageline = Image.open(fotoline)

        listatexto = ['Essa foi boa amigo', 'Vou mimir', 'Hey hey gatinha', 'Oi casada', 'Minha regra é clara, se\nenvolve transar não vale\na pena', 
        'Bom dia cambada dia de\ncheirar pó', 'Hey hey gatinha passa o zap', 'Eu tenho muita sorte de ser\nperfeito, ta ligado?', 
        'Um gostosão como eu ninguém\nresiste não é mesmo?']
        
        textorandom = random.choice(listatexto)
        textorandom2 = textorandom.split()
        textorandom3 = ' '.join(textorandom2)

        fontline = ImageFont.truetype("arial.ttf", 80)
        if textorandom == listatexto[-1]:
            fontline = ImageFont.truetype("arial.ttf", 75)
        color = (255, 255, 255)

        imageline = imageline.resize((1080, 1080))
        drawline = ImageDraw.Draw(imageline)
        drawline.multiline_text((000, 000), (textorandom),fill=(color), font=fontline)


        imageline.save('amigotimeline.png')

        api.update_with_media ('amigotimeline.png', (textorandom3))
        print ("(Tweet enviado na timeline)")
        time.sleep(82.800)

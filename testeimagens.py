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
        listatimeline = ['1.png', '2.png', '3.png', '4.png', '5.jpeg', '6.png', '7.jpeg', '8.png', '9.png', '10.png', '11.jpeg', 
        '12.png', '13.png', '14.png', '15.png', '16.png']
        fotoline = random.choice(listatimeline)
        imageline = Image.open(fotoline)

        listatexto = ['Essa foi boa amigo', 'Vou mimir', 'Hey hey gatinha', 'Oi casada', 'Já passou da hora de mimir', 'Gostosa', 'Ovo', 
        'Bom dia cambada dia de\ncheirar pó', 'Não concordo nem discordo,\nmuito pelo contrário, apenas\ndiscordo', 'O sol nasce, a bicicleta anda,\n o lobo uiva e o urso panda']
        
        textorandom = random.choice(listatexto)

        fontline = ImageFont.truetype("arial.ttf", 80)

        imageline = imageline.resize((1080, 1080))
        drawline = ImageDraw.Draw(imageline)
        drawline.multiline_text((000, 000), (textorandom),fill=(255, 255, 255), font=fontline)


        imageline.save('amigotimeline.png')

        api.update_with_media ('amigotimeline.png', (textorandom))
        print ("(Tweet enviado na timeline)")
        time.sleep(82.800)

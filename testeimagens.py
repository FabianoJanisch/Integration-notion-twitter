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
        listatimeline = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.jpg', '7.png', '8.png', '9.png', '10.png', '11.png', 
        '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png']
        fotoline = random.choice(listatimeline)
        imageline = Image.open(fotoline)

        listatexto = ['    Quem da golpe é lutador\neu sou tipo itaú, feito pra você', 'O que você falou de crepúsculo?? Grr', 'Quando sua mãe fala que quer o\nmelhor pra vc, ela ta falando de mim', 
        'Não mande cantada pra me\nconquistar, me manda um pix', 'Pipipipipipipi... Detector de princesa\n                   ativou aqui', 
        "          Bom dia para meus\n               Jacob'lovers", 'Seu cafuné era tudo que eu\n            queria agora']
        if hora[6] == 4:
            listatexto = ["Bom dia hoje tem sexta dos\ncria", "Sextou com S de cheirar cola"]
        
        textorandom = random.choice(listatexto)
        textorandomR = textorandom.replace ('.', '')
        textorandom2 = textorandom.split()
        textorandom3 = ' '.join(textorandom2)

        color = (255, 255, 255)
        fontline = ImageFont.truetype("arial.ttf", 80)
        if "Pipipipipipipi..." in textorandom or "Quando sua mãe fala" in textorandom:
            fontline = ImageFont.truetype("arial.ttf", 66)
        if 'O que você falou de crepúsculo' in textorandom:
            fontline = ImageFont.truetype("arial.ttf", 63)
            color = (255, 0, 0)


        imageline = imageline.resize((1080, 1080))
        drawline = ImageDraw.Draw(imageline)
        drawline.multiline_text((000, 000), (textorandomR),fill=(color), font=fontline)


        imageline.save('amigotimeline.png')

        api.update_with_media ('amigotimeline.png', (textorandom3))
        print ("(Tweet enviado na timeline)")
        time.sleep(82.800)

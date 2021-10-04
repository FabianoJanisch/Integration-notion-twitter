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
        listatimeline = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', 
        '12.png', '13.png', '14.png', '15.png', '16.png', '17.png']
        fotoline = random.choice(listatimeline)
        imageline = Image.open(fotoline)

        listatexto = ['QUEM É ESSE GOSTOSO??\n                ata sou eu', 'tt = twitter\nttk = tiktok\nig = instagram\nvc = quer namorar comigo?', '    Como que eu vou mandar bom dia\npra ela, se ela só acorda depois das 12h', 
        'Do que adianta ter duas mãos,se vc não\n   vai usar nenhuma pra me dar carinho', ' Dorme bem, pq francamente...\n          boa noite só comigo', 
        'Quero nada sério com você não,\n  só casar e morar junto ta bom', '         E fora da internet?\n      vamos ficar quando??']
        if hora[6] == 4:
            listatexto = ["Bom dia hoje tem sexta dos\ncria", " Sextou, mas qual a graça de\n         sextar sem você??"]
        
        textorandom = random.choice(listatexto)
        textorandomR = textorandom.replace ('.', '')
        textorandom2 = textorandom.split()
        textorandom3 = ' '.join(textorandom2)

        color = (255, 255, 255)
        fontline = ImageFont.truetype("arial.ttf", 80)
        if 'relacionamento dar' in textorandom or "pq francamente" in textorandom:
            fontline = ImageFont.truetype("arial.ttf", 75)
        if "morar junto ta" in textorandom:
            fontline = ImageFont.truetype("arial.ttf", 74)
        if 'depois das 12h' in textorandom or 'nenhuma pra me' in textorandom:
            fontline = ImageFont.truetype("arial.ttf", 60)


        imageline = imageline.resize((1080, 1080))
        drawline = ImageDraw.Draw(imageline)
        drawline.multiline_text((000, 000), (textorandomR),fill=(color), font=fontline)


        imageline.save('amigotimeline.png')

        api.update_with_media ('amigotimeline.png', (textorandom3))
        print ("(Tweet enviado na timeline)")
        time.sleep(82.800)

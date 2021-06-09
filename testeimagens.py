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

        listatexto = ['Vou te levar para ver os incríveis...\nos incríveis beijos que quero te dar', 'Se eu fosse um super herói\nmeu poder ia ser querer ter vc', 'Para o relacionamento dar certo\n os dois tem que ser eu e vc bb', 
        '       Eu até casaria comigo\n     mas essa honra eu deixo\n                   pra vc', 'Sim eu sou gótico...\n\n\nGamado em você\n\nOuvinte da tua linda voz\n\nTe amo\n\nIndignado por tanta beleza\n\nCom seu sorriso eu desmaio\n\nOu vamo namora', 
        'Eu fui no médico e ele falou que\n       preciso de uma vitamina\n               chamada vc', 'Você não é raiz quadrada de 16\n     mas queria sempre poder\n          te deixar de quatro']
        if hora[6] == 4:
            listatexto = ["Bom dia hoje tem sexta dos\ncria", " Sextou, mas qual a graça de\n         sextar sem você??"]
        
        textorandom = random.choice(listatexto)
        textorandomR = textorandom.replace ('.', '')
        textorandom2 = textorandom.split()
        textorandom3 = ' '.join(textorandom2)

        color = (255, 255, 255)
        fontline = ImageFont.truetype("arial.ttf", 80)
        if "os incríveis" in textorandom or "Quando sua mãe fala" in textorandom:
            fontline = ImageFont.truetype("arial.ttf", 69)
        if 'relacionamento dar' in textorandom or "fui no médico" in textorandom or "deixar de quatro" in textorandom:
            fontline = ImageFont.truetype("arial.ttf", 75)


        imageline = imageline.resize((1080, 1080))
        drawline = ImageDraw.Draw(imageline)
        drawline.multiline_text((000, 000), (textorandomR),fill=(color), font=fontline)


        imageline.save('amigotimeline.png')

        api.update_with_media ('amigotimeline.png', (textorandom3))
        print ("(Tweet enviado na timeline)")
        time.sleep(82.800)

import requests
import json
from random import randint
from bs4 import BeautifulSoup



def DownloadImage():
    NOTION_KEY = "secret_iZowESNGYt5uQqaCFNjwk7WrD3gNoGKaGs1OYsVPhaB"
    databaseId = '647a9057c41049519cc14914f44e8495'
    headers =  {
        "Authorization": "Bearer " + NOTION_KEY,
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16"
    }

    #Request site
    readUrl = f'https://api.notion.com/v1/databases/{databaseId}/query'
    res = requests.request("POST", readUrl, headers=headers)
    data2 = BeautifulSoup(res.content, "html.parser").text
    soup = json.loads(data2)

    #Random number
    numbersimage =  len(soup['results'])
    randomizeimage = randint(0, numbersimage-1)

    #Localize image
    urlPage = soup['results'][randomizeimage]['url'].split('-')[-1]
    urlPageC = f'https://api.notion.com/v1/blocks/{urlPage}/children'
    resquestImage = requests.get(urlPageC, headers=headers)
    ImageD = BeautifulSoup(resquestImage.content, "html.parser").text
    soupImageD = json.loads(ImageD)

    #Download image
    ImageDownload = soupImageD['results'][0]['image']['file']['url']
    ImageOpen = open('IMGDownload.png', 'wb')
    responseIMG = requests.get(ImageDownload)
    ImageOpen.write(responseIMG.content)
    ImageOpen.close()



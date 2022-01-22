import requests
import json
from random import randint
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
NOTION_KEY = os.getenv('NOTION_KEY')


def RandomizePhrase():
    databaseId = 'b512d2ddaf7844d091fc16eb9b5f5318'
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
    numbersR =  len(soup['results'])
    randomize = randint(0, numbersR-1)

    #RandomizeAnswer
    phrase = soup['results'][randomize]['properties']['Name']['title'][0]['text']['content']
    fontTTF = soup['results'][randomize]['properties']['Font']['rich_text'][0]['text']['content']
    fontSize = soup['results'][randomize]['properties']['Font size']['number']
    fontColor = soup['results'][randomize]['properties']['Font color']['rich_text'][0]['text']['content']
    lastPost = soup['results'][randomize]['properties']['Last post w/ phrase']['date']['start']


    return (phrase, fontTTF, fontSize, fontColor, lastPost)


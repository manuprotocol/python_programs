# this is the akhbar padhke dekho project

import requests
import json
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

data = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2021-03-11&sortBy=publishedAt&apiKey=2c3945eb4584482498365441abb366a0')

json_data = data.text
print(json_data)
parsed_data = json.loads(json_data)
print(type(parsed_data))

for i in range(1, 10+1):

    final_data = parsed_data["articles"][i]["description"]
    print(final_data)

    speak(final_data)




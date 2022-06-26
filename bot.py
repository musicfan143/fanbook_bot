import requests    
import websocket
import json
import os

def send_message(chat_id, message):
  token = os.getenv('TOKEN')
  url = f'https://a1.fanbook.mobi/api/bot/{token}/sendMessage'
  data = {"chat_id": chat_id, "text": message}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)
  print(r.text)
  return r.text

def processMessage(message):
  pass

def processUpdates():
  url = f'https://a1.fanbook.mobi/api/bot/{TOKEN}/getUpdates'
  data = {"timeout": 60, "limit": 100}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)
  # print(r.text)
  data = json.loads(r.text)
  messages = data['result']
  for message in messages:
    print("-----")
    print(message)

def setPrivacy():
  url = f'https://a1.fanbook.mobi/api/bot/{TOKEN}/setBotPrivacyMode'
  data = {"owner_id": OWNER_ID, "bot_id": BOT_ID, "enable": True}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)
  print(r.text)

def getBot():
  url = f'https://a1.fanbook.mobi/api/bot/{TOKEN}/getMe'
  data = {}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)
  print(r.text)

if __name__ == "__main__":
 while True:
  processUpdates()
  time.sleep(10)

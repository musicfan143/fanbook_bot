import requests    
import websocket
import rel
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

def on_message(ws, message):
    print(message)
    # logic to match the message

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
  # send_message(CHAT_ID, "Test")
  websocket.enableTrace(True)
  token = os.getenv('TOKEN')
  ws = websocket.WebSocketApp(f"wss://a1.fanbook.mobi/api/bot/{token}/getUpdates",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

  ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
  rel.signal(2, rel.abort)  # Keyboard Interrupt
  rel.dispatch()

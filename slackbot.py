import requests
import json

mensagem = {"text": "Olá, esse é um teste de um robô via python!"}
weebhook = " "

requests.post(weebhook, data=json.dumps(mensagem))

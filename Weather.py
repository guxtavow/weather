import requests

def previsao_tempo(cidade,chave_API):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt-br&appid={chave_API}&units=metric"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

chave_API = '8cb49412f1ef8c97bb90407146a8988b'
cidade = 'São Paulo'

previsao = previsao_tempo(cidade, chave_API)

if previsao['cod'] == 200:
    print(f'Clima atual em {cidade} é: {previsao['weather'][0]['description']}')
    print(f'Temperatura atual de: {round(previsao['main']['temp'])}°C')
else:
    print("Cidade não encontrada!")
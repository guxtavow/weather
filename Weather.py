import requests
import geocoder
import tkinter as tk


def previsao_tempo(cidade,chave_API):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_API}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def previsao_tempo_atual(cidadeAtual,chave_API):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidadeAtual}&appid={chave_API}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    dados = resposta.json()
    print(dados)
    return dados

def Local():
    g = geocoder.ip('me')  # 'me' irá usar o IP do usuário atual
    g.city
    cidadeAtual = g.city
    return cidadeAtual
    

opcoes = input("Opções:\n1-Escolher cidade de minha preferencia\n2-Minha cidade atual\nDigite sua opção(ATENÇÃO: Apenas digite o numero):")


chave_API = '8cb49412f1ef8c97bb90407146a8988b'
previsao = previsao_tempo_atual(Local(), chave_API)



try:
    if opcoes == "1":
        saber_Local = input("Qual cidade você quer saber o clima?: ")
        cidade = saber_Local.title()
        previsao = previsao_tempo(cidade, chave_API)

        if previsao['cod'] == 200:
                print()
                print("*********************************************************")
                print(f'Clima atual em {cidade} é: {(previsao['weather'][0]['description']).title()}') #Title para sair com a string formatada
                print(f'Temperatura atual de: {round(previsao['main']['temp'])}°C') #arredondo o numero da temperatura
                print(f'Sensação térmica de: {round(previsao['main']['feels_like'])}°C')
                print(f'Com máximas de: {round(previsao['main']['temp_max'])}°C')
                print(f'E mínimas de: {round(previsao['main']['temp_min'])}°C')
                print("*********************************************************")
                print()
        else:
            print("Cidade não encontrada!")
    elif opcoes == "2":
        print()
        print("*********************************************************")
        print(f'Sua localização é: {Local()}')
        print(f'Clima atual em {Local()} é: {previsao['weather'][0]['description']}')
        print(f'Temperatura atual de: {round(previsao['main']['temp'])}°C')
        print(f'Sensação térmica de: {round(previsao['main']['feels_like'])}°C')
        print(f'Com máximas de: {round(previsao['main']['temp_max'])}°C')
        print(f'E mínimas de: {round(previsao['main']['temp_min'])}°C')
        print("*********************************************************")
        print()
    else:
        print('Opção invalida')
except:
    print('error')
    

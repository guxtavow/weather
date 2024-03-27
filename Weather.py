import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def previsao_tempo(cidade,chave_API):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_API}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def previsao_tempo_atual(latitude,longitude,chave_API):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={chave_API}&units=metric"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def get_current_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        # Tenta obter a localização atual
        location = geolocator.geocode("me")
        if location:
            print("Latitude e Longitude:", (location.latitude, location.longitude))
            print("Endereço:", location.address)
        else:
            print("Não foi possível obter a localização atual.")
    except GeocoderTimedOut:
        print("Tempo esgotado. Não foi possível obter a localização atual.")

if __name__ == "__main__":
    get_current_location()



opcoes = input("Opções:\n1-escolher cidade atual\n2-escolher cidade de minha preferencia\nDigite sua opção(ATENÇÃO: Apenas digite o numero):")


chave_API = '8cb49412f1ef8c97bb90407146a8988b'


if opcoes == "1":
    saber_Local = input("Qual cidade você quer saber o clima?: ")
    cidade = saber_Local.title()
    previsao = previsao_tempo(cidade, chave_API)

    if previsao['cod'] == 200:
            print(f'Clima atual em {cidade} é: {previsao['weather'][0]['description']}')
            print(f'Temperatura atual de: {round(previsao['main']['temp'])}°C')
    else:
        print("Cidade não encontrada!")
elif opcoes == "2":
     latitude, longitude = get_current_location()

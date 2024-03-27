import socket
import requests


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f'O endereço IP da sua máquina é: {ip_address}')




def get_location_from_ip(ip):
    try:
        url = f"http://ipinfo.io/{ip}/json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Erro ao obter informações de localização. Código de status:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Erro de conexão:", e)
        return None

# Substitua 'seu_endereco_ip' pelo endereço IP que você deseja localizar
location_info = get_location_from_ip(ip_address)
if location_info is not None:
    print("Localização estimada:")
    print("IP:", location_info.get("ip"))
    print("Cidade:", location_info.get("city"))
    print("Região:", location_info.get("region"))
    print("País:", location_info.get("country"))
    print("Coordenadas:", location_info.get("loc"))
else:
    print("Não foi possível obter informações de localização.")
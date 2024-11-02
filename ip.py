import os
import requests
from pystyle import Colors, Colorate, Center

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data
        else:
            return "Информация по IP не найдена."
    else:
        return "Не удалось подключиться к API."

banner = """
Поиск по IP
"""

def main():
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(banner)))
    ip = input(Colorate.Horizontal(Colors.green_to_white, "\nВведите IP для поиска: "))
    result = search_ip(ip)
    
    if isinstance(result, str):
        print(Colorate.Horizontal(Colors.green_to_white, f"\n{result}"))
    else:
        print(Colorate.Horizontal(Colors.green_to_white, f"""
        IP: {result.get('query')}
        Страна: {result.get('country')}
        Регион: {result.get('regionName')}
        Город: {result.get('city')}
        ZIP: {result.get('zip')}
        Широта: {result.get('lat')}
        Долгота: {result.get('lon')}
        Провайдер: {result.get('isp')}
        Организация: {result.get('org')}
        """))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))
    clear_console()

if __name__ == "__main__":
    main()
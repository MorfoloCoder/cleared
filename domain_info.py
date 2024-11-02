import whois
import sys

def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"Ошибка при получении информации о домене: {e}"

def main():
    domain = input("Введите домен для поиска: ")
    info = get_domain_info(domain)
    print(f"\nИнформация о домене {domain}:\n{info}")

if __name__ == "__main__":
    main()

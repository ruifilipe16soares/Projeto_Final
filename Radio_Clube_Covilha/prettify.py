import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        # Faz o pedido GET ao site
        response = requests.get(url)
        # Verifica se o pedido foi bem sucedido
        response.raise_for_status()
        # Obtém o conteúdo HTML
        html = response.text
        return html
    except Exception as e:
        print("Ocorreu um erro ao obter o HTML:", e)
        return None

def prettify_html(html):
    try:
        # Cria um objeto BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Organiza o HTML de forma mais legível
        prettified_html = soup.prettify()
        return prettified_html
    except Exception as e:
        print("Ocorreu um erro ao organizar o HTML:", e)
        return None

if __name__ == "__main__":
    # URL do site que você quer obter o HTML
    url = input("Insira a URL do site: ")
    # Obtém o HTML do site
    html = get_html(url)
    if html:
        # Organiza o HTML de forma mais legível
        prettified_html = prettify_html(html)
        if prettified_html:
            print(prettified_html)

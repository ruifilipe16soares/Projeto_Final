import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_news_content(url):
    """
    Função para extrair os links das notícias de uma URL específica.
    """
    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')
        link = site.find_all('a', href=True)
        if link:
            for l in link:
                href = l['href']
                if "mailto" not in href and "pesquisa" not in href:
                    news_url = urljoin(url, href)
                    links.append(news_url)
        else:
            print(f'Nenhuma notícia encontrada em {url}')
            return None
    else:
        print(f'Falha ao acessar {url}')
        return None

# Nome do arquivo CSV
csv_filename = 'links_RCC.csv'
csv_filename_2 = 'links_noticias_RCC_02_05.csv'

linha_inicio = 14
linha_fim = 63

# Lista para armazenar os links das notícias
links = []

# Abrir o arquivo CSV e iterar sobre as linhas
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for idx, row in enumerate(reader):
        if linha_inicio <= idx + 1 <= linha_fim:
            url = row['URL']
            content = extract_news_content(url)
            if content:
                links.append(content)

# Salvar os dados no arquivo CSV
with open(csv_filename_2, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Links'])
    for link in links:
        writer.writerow([link])

print("Links das notícias salvos em", csv_filename_2)
import csv
import requests
from bs4 import BeautifulSoup

def extract_news_content(url):
    """
    Função para extrair o conteúdo da notícia de uma URL específica.
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')
        
        # Tentar encontrar notícias com diferentes classes
        noticia = site.find_all('h4', class_='title')
        
        if noticia:
                #return [item.text.strip() for item in noticia[1:]]
            for noticia_item in noticia:
                link = noticia_item.find('a', class_='term-85', href=True) #se nao der tira o 'a'
                if link:
                    news_url = link['href']
                    links.append(news_url)
        else:
            print(f'Nenhuma notícia encontrada em {url}')
            return None
    else:
        print(f'Falha ao acessar {url}')
        return None

# Nome do arquivo CSV
#csv_filename = 'links_NC_finais.csv'
csv_filename = 'links_NC_finais.csv'
csv_filename_2 = 'links_noticias_NC_19_23.csv'



linha_inicio = 2758
linha_fim = 4064
#2066

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
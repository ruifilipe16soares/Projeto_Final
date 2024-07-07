import csv
import json
import requests
from bs4 import BeautifulSoup


def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')


        #titulo = site.find('div', class_='art-postmetadataheader')
        titulo = site.find('h1', class_='entry-title entry--item h2')
        section = site.find('span', class_='meta-item meta-cat') 
        subtitulo = site.find('p', class_ ='subtitulo') #nao tem 
        texto = site.find('div', class_='entry-content entry--item')
        data = site.find('time', class_='entry-date published')
        autor = site.find('span', class_='author vcard')
        foto = site.find('img')['src']

        titulo_texto = titulo.text.strip() if titulo else ""
        section_texto = section.text.strip() if section else ""
        subtitulo_texto = subtitulo.text.strip() if subtitulo else ""
        texto_texto = texto.text.strip() if texto else ""
        data_texto = data.text.strip() if data else ""
        autor_texto = autor.text.strip() if autor else ""
        foto_texto = foto.strip() if foto else ""

            # Armazenar os dados em um dicionário
        noticia_dict = {
            "titulo": titulo_texto,
            "section": section_texto,
            "subtitulo": subtitulo_texto,
            "texto": texto_texto,
            "data": data_texto,
            "autor": autor_texto,
            "foto": foto_texto,
            "link": url
        }
        noticias.append(noticia_dict)
    else:
        #print(f'Falha ao acessar {url}')
        return None

# Nome do arquivo CSV
csv_filename = 'links_noticias_RC_20_22.csv'
json_filename = 'noticiasRC_20_22.json'

#linha_inicio = 63
#linha_fim = 101

# Lista para armazenar os dados das notícias
noticias = []

# Abrir o arquivo CSV e iterar sobre as linhas
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['Links']
        content = extract_news_content(url)
        if content:
            noticias.append(content)

# Salvar os dados no arquivo JSON
with open(json_filename, 'w', encoding='utf-8') as jsonfile:
    json.dump(noticias, jsonfile, ensure_ascii=False, indent=4)

print("Dados das notícias salvos em", json_filename)


import csv
import json
import requests
from bs4 import BeautifulSoup

def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')


        titulo = site.find('h2', class_='art-postheader')
        section = site.find('div', class_='categoriaData') #nao tem
        subtitulo = site.find('div', class_='superlead') #nao tem
        texto = site.find('div', class_='art-article')
        data = site.find('span', class_='art-postdateicon')
        autor = site.find('span', class_='art-postauthoricon')
        foto = site.find('img')['src']

        titulo_texto = titulo.text.strip() if titulo else ""
        section_texto = section.text.strip() if section else ""
        subtitulo_texto = subtitulo.text.strip() if subtitulo else ""
        texto_texto = texto.text.strip() if texto else ""
        data_texto = data.text.strip() if data else ""
        autor_texto = autor.text.strip() if autor else ""
        foto_texto = foto.strip() if foto else ""

        if ":" in data_texto:
            data_texto_fin = data_texto[:-6]
        else:
            data_texto_fin = data_texto

            # Armazenar os dados em um dicionário
        noticia_dict = {
            "titulo": titulo_texto,
            "section": section_texto,
            "subtitulo": subtitulo_texto,
            "texto": texto_texto,
            "data": data_texto_fin[13:],
            "autor": autor_texto[12:],
            "foto": foto_texto if 'https://arquivo.pt/noFrame/' in foto_texto else "",
            "link": url
        }
        noticias.append(noticia_dict)
    else:
        #print(f'Falha ao acessar {url}')
        return None

# Nome do arquivo CSV
csv_filename = 'filtered_RC_16_19.csv'
json_filename = 'noticiasRC_16_19.json'

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


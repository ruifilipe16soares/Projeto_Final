import csv
import json
import requests
from bs4 import BeautifulSoup

def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')

        titulo = site.find('div', class_='titulo')
        section = site.find('div', class_='categoriaData')
        subtitulo = site.find('div', class_='superlead')
        texto = site.find('div', class_='corpo')
        data = site.find('div', class_='data')
        autor = site.find('div', class_='jornalistas')
        foto = site.find('div', class_='foto')
        foto_fin = foto.find('img')['src'] if foto else ""

        titulo_texto = titulo.text.strip() if titulo else ""
        section_texto = section.text.strip() if section else ""
        subtitulo_texto = subtitulo.text.strip() if subtitulo else ""
        texto_texto = texto.text.strip() if texto else ""
        data_texto = ""
        if data:
            if "há" not in data.text and "ontem" not in data.text:
                data_texto = data.text.strip()

        autor_texto = autor.text.strip() if autor else ""
        foto_texto = foto_fin.strip() if foto else ""

        if data_texto != "":
            data_fin = data_texto
            autor_fin = autor_texto
        elif data_texto == "" and "de 20" in autor_texto:
            data_fin = autor_texto[-17:]
            autor_fin = autor_texto[:-21]
        else:
            data_fin = ""
            autor_fin = ""

            # Armazenar os dados em um dicionário
        noticia_dict = {
            "titulo": titulo_texto,
            "section": section_texto,
            "subtitulo": subtitulo_texto,
            "texto": texto_texto,
            "data": data_fin,
            "autor": autor_fin[4:],
            "foto": foto_texto,
            "link": url
        }
        noticias.append(noticia_dict)
    else:
        #print(f'Falha ao acessar {url}')
        return None

# Nome do arquivo CSV
csv_filename = 'filtered_RCB_12_23_parte_12.csv'
json_filename = 'noticiasRCB_23_12.json'

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


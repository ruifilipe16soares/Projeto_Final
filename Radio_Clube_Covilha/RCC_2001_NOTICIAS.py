import csv
import json
import requests
from bs4 import BeautifulSoup

def extract_news_content(url):    
    response = requests.get(url) 
    if response.status_code == 200:
        content = response.content.decode('latin-1', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')

        titulo = ""
        section = site.find('div', class_='titulo_destaque') #nao tem
        subtitulo = site.find('div', class_='texto') #nao tem
        texto = ""
        data = ""
        autor = site.find('div', class_='jornalista') #nao tem
        foto = site.find('div', class_='fot') #nao tem
        noticia = site.find_all('p')

        if noticia:
            for p in noticia:
                texto = p
        else:
            texto = ""

        data_tit = site.find('p')
        data = data_tit.find('font') if data_tit else ""
        titulos = data_tit.find_all('font') if data_tit else ""
        if titulos:
            for tit in titulos:
                titulo = tit
        else:
            titulo = ""


        titulo_texto = titulo.text.strip() if titulo else ""
        section_texto = section.text.strip() if section else ""
        subtitulo_texto = subtitulo.text.strip() if subtitulo else ""
        texto_texto = texto.text.strip() if texto else ""
        data_texto = data.text.strip() if data else ""
        autor_texto = autor.text.strip() if autor else ""
        foto_texto = foto.text.strip() if foto else ""

            # Armazenar os dados em um dicionário
        noticia_dict = {
            "titulo": titulo_texto,
            "section": section_texto,
            "subtitulo": subtitulo_texto,
            "texto": texto_texto,
            "data": data_texto[:10],
            "autor": autor_texto,
            "foto": foto_texto,
            "link": url
        }
        noticias.append(noticia_dict)
    else:
        #print(f'Falha ao acessar {url}')
        return None

# Nome do arquivo CSV
csv_filename = 'links_noticias_RCC_01.csv'
json_filename = 'noticiasRCC_1.json'

#linha_inicio = 63
#linha_fim = 101

# Lista para armazenar os dados das notícias
noticias = []

# Abrir o arquivo CSV e iterar sobre as linhas
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['Links']
        if not url.startswith(('https://')):
            continue
        content = extract_news_content(url)
        if content:
            noticias.append(content)

# Salvar os dados no arquivo JSON
with open(json_filename, 'w', encoding='utf-8') as jsonfile:
    json.dump(noticias, jsonfile, ensure_ascii=False, indent=4)

print("Dados das notícias salvos em", json_filename)


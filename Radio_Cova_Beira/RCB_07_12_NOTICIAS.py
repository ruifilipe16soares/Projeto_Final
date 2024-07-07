import csv
import json
import requests
from bs4 import BeautifulSoup

def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('latin-1', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')
        """
        noticia = site.find_all('tr', class_="tabela_titulos")
        if noticia:
            for noticia_item in noticia:
                link_noticia = noticia_item.find('a')['href']
                return link_noticia
        else:
            #print(f'Nenhuma notícia encontrada em {url}')
            return None
            """
        titulo = site.find('div', class_='titulo')
        section = site.find('div', class_='titulo_destaque')
        subtitulo = site.find('div', class_='texto')
        texto = site.find('td', class_='texto')
        data = site.find('div', class_='texto light')
        autor = site.find('div', class_='jornalista')
        foto = site.find('div', class_="ft")

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
csv_filename = 'links_noticias_RCB_07_12.csv'
json_filename = 'noticiasRCB_1_2_2.json'

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


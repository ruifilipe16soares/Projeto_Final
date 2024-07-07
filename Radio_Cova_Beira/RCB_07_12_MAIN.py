import csv
import json
import requests
from bs4 import BeautifulSoup

def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('latin-1', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')
        
        
        noticia = site.find_all('tr', class_="tabela_titulos")
        if noticia:
            for noticia_item in noticia:
                titulo = noticia_item.find('div', class_='titulo')
                section = noticia_item.find('div', class_='titulo_destaque')
                subtitulo = noticia_item.find('div', class_='texto')
                texto = noticia_item.find('td', class_='t')
                data = noticia_item.find('div', class_='texto light')
                autor = noticia_item.find('div', class_='j')
                foto = site.find('div', class_="ft")

                titulo_texto = titulo.text.strip() if titulo else ""
                section_texto = section.text.strip() if section else ""
                subtitulo_texto = ""
                texto_texto = texto.text.strip() if texto else ""
                data_texto = data.text.strip() if data else subtitulo.text.strip()[-12:]
                autor_texto = autor.text.strip() if autor else ""
                foto_texto = foto.text.strip() if foto else ""

                data_texto_fin = ""

                if "·" in data_texto and "\r\n" not in data_texto:
                    data_texto_fin = data_texto[:-17] + "]"
                elif "·" in data_texto and "\r\n" in data_texto:
                    data_texto_fin = data_texto[:-27] + "]"
                else:
                    data_texto_fin = data_texto

                
                #if not data:
                    #data_texto = subtitulo.text.strip()[-12:]
                    #subtitulo_texto = subtitulo.text.strip()[:-12]

                                # Armazenar os dados em um dicionário
                noticia_dict = {
                    "titulo": titulo_texto,
                    "section": section_texto,
                    "subtitulo": subtitulo_texto,
                    "texto": texto_texto,
                    "data": data_texto_fin,
                    "autor": autor_texto,
                    "foto": foto_texto,
                    "link": ""
                }
                noticias.append(noticia_dict)
        
        else:
            #print(f'Nenhuma notícia encontrada em {url}')
            return None
            
# Nome do arquivo CSV
csv_filename = 'links_RCB.csv'
json_filename = 'noticiasRCB_1_1_1.json'

linha_inicio = 63
linha_fim = 101

# Lista para armazenar os dados das notícias
noticias = []

# Abrir o arquivo CSV e iterar sobre as linhas
with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for idx, row in enumerate(reader):
        if linha_inicio <= idx + 1 <= linha_fim:
            url = row['URL']
            content = extract_news_content(url)
            if content:
                noticias.append(content)

# Salvar os dados no arquivo JSON
with open(json_filename, 'w', encoding='utf-8') as jsonfile:
    json.dump(noticias, jsonfile, ensure_ascii=False, indent=4)

print("Dados das notícias salvos em", json_filename)


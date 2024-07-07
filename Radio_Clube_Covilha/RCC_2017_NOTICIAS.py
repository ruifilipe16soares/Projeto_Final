import csv
import json
import requests
from bs4 import BeautifulSoup
import re

def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')

        noticia = site.find('div', id='primary', class_='content-area')

        if noticia:
                titulo = noticia.find('h1', class_='entry-title')
                section = noticia.find('span', class_='cat-links')
                subtitulo = noticia.find('div', class_='texto') #nao há subtitulo
                texto = noticia.find('div', class_='entry-content')
                paragrafos = texto.find_all('p')
                texto_texto = ""

                if paragrafos:
                    for p in paragrafos:
                        texto_texto += p.get_text().strip() + " "
                else:
                    paragrafos = ""

                data = noticia.find('span', class_='posted-on')

                autor2 = noticia.find('a', class_="url fn n")
                foto = noticia.find('img')

                titulo_texto = titulo.text.strip() if titulo else ""
                section_texto = section.text.strip() if section else ""
                subtitulo_texto = subtitulo.text.strip() if subtitulo else ""
                texto_texto = texto_texto.strip() if texto else ""
                data_texto = data.text.strip() if data else ""
                autor_texto = autor2.text.strip() if autor2 else ""
                foto_texto = foto['src'] if foto else ""


                if texto_texto:
                    if "Por:" in texto_texto.split()[-3:]:
                        palavras = texto_texto.split()
                        autor_texto = ' '.join(palavras[-2:]) if autor_texto else ""
                    else:
                        autor_texto = autor2.text.strip() if autor_texto else ""
                else:
                    texto_texto = ""

                match = re.match(r'([A-Za-z]+ \d{1,2}, \d{4})', data_texto)
                if match:
                    data_texto = match.group(1)



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

    else:
        #print(f'Nenhuma notícia encontrada em {url}')
        return None



# Nome do arquivo CSV
csv_filename = 'filtered_RCC_17_parte_3.csv'
json_filename = 'noticiasRCC_3_3_3.json'

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



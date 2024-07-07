import csv
import json
import requests
from bs4 import BeautifulSoup

def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')
        site = BeautifulSoup(content, 'html.parser')

        noticia = site.find('div', class_='main col-md-8')

        if noticia:
                titulo = noticia.find('h1', itemprop='headline')
                section = noticia.find('a', class_='term-7') #pode ou nao haver
                subtitulo = noticia.find('div', class_='bk-post-subtitle') #pode haver ou nao subtitulo
                texto = noticia.find('div', class_='article-content clearfix')
                data = noticia.find('div', class_='post-date')
                autor = noticia.find('div', class_='post-author')
                f = noticia.find('div', class_='s-feat-img') 
                foto_texto = f.find('img')['src'] if f else ""


                titulo_texto = titulo.text.strip() if titulo else ""
                section_texto = section.text.strip() if section else ""
                subtitulo_texto = subtitulo.text.strip() if subtitulo else ""
                texto_texto = texto.text.strip() if texto else ""
                data_texto = data.text.strip() if data else ""
                autor_texto = autor.text.strip() if autor else ""

                if not foto_texto.startswith('http'):
                    foto_texto = ""

                if section_texto.lower() == "desporto":
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
                    return None
        else:
            #print(f'Falha ao acessar {url}')
            return None

    else:
        #print(f'Nenhuma notícia encontrada em {url}')
        return None



# Nome do arquivo CSV
csv_filename = 'final_links_19_23_parte_2.csv'
json_filename = 'NC_19_23_2.json'

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



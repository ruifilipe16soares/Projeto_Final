import csv
import json
import requests
from bs4 import BeautifulSoup
import chardet

def extract_news_content(url):    
    response = requests.get(url)
    if response.status_code == 200:
        detected_encoding = chardet.detect(response.content)['encoding']
        content = response.content.decode(detected_encoding, errors='ignore')
        site = BeautifulSoup(content, 'html.parser')

        noticia = site.find('div', id='div_conteudo_left')

        if noticia:
                titulo = noticia.find('h1', class_='georgia t38')
                section = site.find('div', id='div_caminho', class_='georgia t12')
                section1 = section.find('a', href=True) if section else ""
                section2 = section1.find('b') if section1 else ""
                subtitulo = noticia.find('div', class_='texto') #nao há subtitulo
                texto = noticia.find('span', id='mtexto')
                data = noticia.find('span', class_='georgia t10 cinza')
                autor = noticia.find('span', class_='t11 cinza italico') 
                foto = noticia.find('img')


                titulo_texto = titulo.text.strip() if titulo else ""
                section_texto = section2.text.strip() if section2 else ""
                subtitulo_texto = subtitulo.text.strip() if subtitulo else ""
                texto_texto = texto.text.strip() if texto else ""
                data_texto = data.text.strip() if data else ""
                autor_texto = autor.text.strip() if autor else ""
                foto_texto = foto['src'] if foto else ""

                if " " in foto_texto:
                    foto_texto = foto_texto.replace(" ", "%20")

                if section_texto.lower() == "desporto":
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
                    return None
        else:
            #print(f'Falha ao acessar {url}')
            return None

    else:
        #print(f'Nenhuma notícia encontrada em {url}')
        return None



# Nome do arquivo CSV
#csv_filename = 'inks_noticias_NC_09_19_parte_1.csv'
csv_filename = 'final_links_09_19.csv'
json_filename = 'NC_09_19.json'


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



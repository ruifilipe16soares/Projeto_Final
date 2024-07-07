import json

# Função para carregar os dados de um arquivo JSON
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Função para combinar as informações das notícias
def combine_news(news1, news2):
    combined_news = {}
    for key in news1:
        if key == 'titulo':
            combined_news[key] = news1[key]
        elif news1[key] != '':
            combined_news[key] = news1[key]
        else:
            combined_news[key] = news2[key]
    return combined_news

# Carregar os dados dos arquivos JSON
file1_data = load_json('noticiasRCB_1_1_1.json')
file2_data = load_json('noticiasRCB_1_2_2.json')

# Criar um dicionário para armazenar as notícias combinadas
combined_news_dict = {}

# Iterar sobre as notícias do primeiro arquivo
for news1 in file1_data:
    # Iterar sobre as notícias do segundo arquivo
    for news2 in file2_data:
        # Se os títulos das notícias forem iguais
        if news1['titulo'] == news2['titulo']:
            # Combinar as informações das notícias
            combined_news = combine_news(news1, news2)
            # Adicionar a notícia combinada ao dicionário
            combined_news_dict[news1['titulo']] = combined_news
            break  # Parar de procurar no segundo arquivo quando encontrar uma correspondência

# Converter o dicionário de notícias combinadas de volta para uma lista
combined_news_list = list(combined_news_dict.values())

# Salvar as notícias combinadas em um novo arquivo JSON
with open('noticiasRCB_07_12.json', 'w', encoding='utf-8') as file:
    json.dump(combined_news_list, file, ensure_ascii=False, indent=4)

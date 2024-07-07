import json

# Função para carregar os dados de um arquivo JSON
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Função para salvar os dados em um arquivo JSON
def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Carregar as notícias existentes do arquivo JSON
noticias1 = load_json('noticiasRCB_23_1.json')
noticias2 = load_json('noticiasRCB_23_2.json')
noticias3 = load_json('noticiasRCB_23_3.json')
noticias4 = load_json('noticiasRCB_23_4.json')
noticias5 = load_json('noticiasRCB_23_5.json')
noticias6 = load_json('noticiasRCB_23_6.json')
noticias7 = load_json('noticiasRCB_23_7.json')
noticias8 = load_json('noticiasRCB_23_8.json')
noticias9 = load_json('noticiasRCB_23_9.json')
noticias10 = load_json('noticiasRCB_23_10.json')
noticias11 = load_json('noticiasRCB_23_11.json')
noticias12 = load_json('noticiasRCB_23_12.json')


noticias13 = load_json('noticiasRCB_ate2007.json')

noticias14 = load_json('noticiasRCB_07_12.json')

# Combinar todas as notícias em uma única lista
all_news = noticias13 + noticias14 + noticias1 + noticias2 + noticias3 + noticias4 + noticias5 + noticias6 + noticias7 + noticias8 + noticias9 + noticias10 + noticias11 + noticias12

# Salvar todas as notícias no mesmo arquivo JSON
save_json(all_news, 'RCB_FINAL.json')
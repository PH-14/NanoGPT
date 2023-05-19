import json


def convert_to_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    articles = []
    current_article = None

    for line in lines:
        line = line.strip()
        if line:
            if line[0] == "A":  # remplacer en fonction du texte utilisé: line[0].isdigit()
                if current_article is not None:
                    articles.append(current_article)
                article_number, article_title = line.split('. ', 1)
                current_article = {
                    'prompt': f"Quels sont les règles de la FCUE concernant : {article_number}. {article_title} ?",
                    'completion': ''
                }
            else:
                current_article['completion'] += " " + line + '\n'

    if current_article is not None:
        articles.append(current_article)

    with open('reglement_fcue2.jsonl', 'w', encoding='utf-8') as jsonl_file:
        for article in articles:
            jsonl_file.write(json.dumps(article, ensure_ascii=False) + '\n')


# Appel de la fonction de conversion
convert_to_jsonl('reglement_fcue2.txt')

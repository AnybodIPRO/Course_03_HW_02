import json
# import candidates.json


FILE_DIR = 'candidates.json'

def load_candidates(FILE_DIR): # которая загрузит данные из файла
    with open(FILE_DIR, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data
"""ниже функция которая возвращает список всех кандидатов"""
def get_all():
    data = load_candidates(FILE_DIR)
    result = ''
    for i in data:
        result += '\n'
        result += i["name"] + '\n'
        result += i["position"] + '\n'
        result += i["skills"] + '\n'
    return (f'<pre> {result} </pre>')


def et_by_pk(pk): # которая вернет кандидата по pk
    data = load_candidates(FILE_DIR)
    candidate = ''

    for i in data:
        if i['pk'] == pk:
            return i
    return ('Кандидат не найден')


def get_by_skill(skill_name): # которая вернет кандидатов по навыку
    data = load_candidates(FILE_DIR)
    candidate_list = []
    for i in data:
        if skill_name.lower() in i['skills'].lower():
            candidate_list.append(i)
    return candidate_list


def get_by_name(candidate_name): # которая вернет кандидатов по имени
    data = load_candidates(FILE_DIR)
    candidate_list = []
    for i in data:
        if candidate_name.lower() in i['name'].lower():
            candidate_list.append(i)
    return candidate_list

print(get_by_skill('python'))

import json
# import candidates.json


FILE_DIR = 'candidates.json'

def load_candidates(FILE_DIR): # которая загрузит данные из файла
    with open(FILE_DIR, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def get_by_skill(skill_name): # которая вернет кандидатов по навыку
    data = load_candidates(FILE_DIR)
    candidate_list = ''
    for i in data:
        if skill_name in i['skills'].lower():
            candidate_list += i['name'] + '\n'
    return candidate_list

print(get_by_skill('python'))
import json
import glob
import os
import shutil
from slugify import slugify


def get_profession():
    try:
        os.mkdir('prof')
    except:
        shutil.rmtree('prof')
        os.mkdir('prof')
    with open('eskd1.txt', 'r') as file:
        key = ''
        for string in file:
            if string[0:3].isupper():
                key = string.strip()
            with open(f'prof/{key}.txt', 'a') as prof:
                prof.write(string)

                
def create_json():
    data = []
    pk = 1
    for prof_file in glob.glob('prof/*.txt'):
        data_dict = {}
        with open(prof_file, 'r') as file:
            prof_name = prof_file.rstrip('.txt').lstrip("prof/")
            prof_description = file.read().lstrip(prof_name)
            data_dict['model'] = 'embase.position'
            data_dict['pk'] = pk
            data_dict['fields'] = {}
            data_dict['fields']['name'] = prof_name.lower().capitalize()
            data_dict['fields']['slug'] = slugify(prof_name.lower().capitalize())
            data_dict['fields']['description'] = prof_description.lstrip("\n")
            data.append(data_dict)
            pk += 1
    with open('professions.json', 'w', encoding='utf8') as json_file:
        json_data = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
        json_file.write(json_data)


if __name__ == '__main__':
    get_profession()
    create_json()
    shutil.rmtree('prof')


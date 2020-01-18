import json

path = "E:\\fiddler\\data\\question.txt"

try:
    with open(path, 'r', encoding='utf-8') as file_object:
        json_str = json.loads(file_object.readline())
        data = json_str['data']
        questions = data['questions']
        for i, q in enumerate(questions):
            print(q['prompt'] + q['answer'])
except FileNotFoundError:
    print("sorry, the file does not exist")

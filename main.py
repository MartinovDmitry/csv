import csv
import requests

url = 'https://jsonplaceholder.typicode.com/users/{userId}/todos'

result = list()

try:
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:  # type: dict
            userId = row.get('userId')
            todo_id = int(row.get('todo_id'))
            response = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}/todos')
            json_response = response.json()
            if len(json_response) != 0:
                dct_with_false = row.copy()
                new_dict = row.copy()
                for dct in json_response:  # type: dict
                    if dct.get('id') == todo_id:
                        new_dict.update(is_owner=True, completed=dct.get('completed'))
                        result.append(new_dict)
                        break
                else:
                    dct_with_false.update(is_owner=False, completed=False)
                    result.append(dct_with_false)
except KeyboardInterrupt as err:
    print(err)


with open('result.csv', 'w') as file:
    fieldnames = ['uuid', 'userId', 'todo_id', 'is_owner', 'completed']
    writer = csv.writer(file, lineterminator="\r")
    dict_writer = csv.DictWriter(file, lineterminator="\r",  fieldnames=fieldnames)
    writer.writerow(fieldnames)
    dict_writer.writerows(result)

# with open('result.csv', 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)

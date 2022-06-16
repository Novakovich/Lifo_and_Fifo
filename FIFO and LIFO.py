import json
def get_goods(file_name):
    with open(file_name, 'r', encoding='utf-8') as f_json:
        some_goods = json.load(f_json)
        return some_goods
STRATEGY = input('LIFO/FIFO')
file = 'd:/LifoAndFifo/data.json'
person_have = input('что у вас?')

while True:
    if person_have == 'exit':
        quit()
    if not person_have:
        if STRATEGY == ('FIFO'):
            goods = get_goods(file)
            fifo_item = goods.pop(0)
            print('Возьмите, вот вам ' + fifo_item['name'] + ' ' + str(fifo_item['amount']) + ' шт')
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(goods, f)
        elif STRATEGY == ('LIFO'):
            goods = get_goods(file)
            lifo_item = goods.pop()
            print('Возьмите, вот вам ' + lifo_item['name'] + ' ' + str(lifo_item['amount']) + ' шт')
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(goods, f)
    if person_have:
        amount = input('сколько?')
        entry = {"name": person_have, "amount": int(amount)}
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data.append(entry)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
            print('Спасибо')
    person_have = input('что у вас?')

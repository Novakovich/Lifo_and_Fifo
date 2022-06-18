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
        break
    if not person_have:
        goods = get_goods(file)
        if STRATEGY == ('FIFO'):
            item = goods.pop(0)
        elif STRATEGY == ('LIFO'):
            item = goods.pop()
        print('Возьмите, вот вам ' + item['name'] + ' ' + str(item['amount']) + ' шт')
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(goods, f)
    if person_have:
        amount = input('сколько?')
        entry = {"name": person_have, "amount": int(amount)}
        goods = get_goods(file)
        goods.append(entry)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(goods, f)
            print('Спасибо')
    person_have = input('что у вас?')

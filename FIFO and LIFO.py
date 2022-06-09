import json
def get_goods(filename):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = file.readlines()
        return data

STRATEGY = input('LIFO/FIFO')
goods = get_goods('d:/LifoAndFifo/data.json')
person_have = input('что у вас?')
amount = input('сколько?')

while len(goods) >= 0:
    if person_have == 'exit':
        quit()
    if not person_have:
        if STRATEGY == ('FIFO'):
            item = goods.pop(0)
            i = item.split()
            print('Возьмите, вот вам', ' '.join(i))
        elif STRATEGY == ('LIFO'):
            item = goods.pop()
            i = item.split()
            print('Возьмите, вот вам', ' '.join(i))
    if person_have and amount:
        with open('d:/LifoAndFifo/data.json', 'a', encoding='utf-8') as f:
            data = {"name": person_have, "amount": int(amount)}
            json.dump(data, f)
            f.write(', ')
            f.close()
            print('Спасибо')
    person_have = input('что у вас?')
    amount = input('сколько?')

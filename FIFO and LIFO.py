
def get_goods(filename):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = file.readlines()
        return data

STRATEGY = input('LIFO/FIFO')
goods = get_goods('d:/LifoAndFifo/data.txt')
person_have = input('что у вас?')
while goods:
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
    if person_have:
        with open('d:/LifoAndFifo/data.txt', 'a', encoding='utf-8') as f:
            f.writelines(['\n' + person_have])
            f.close()
            print('Спасибо')
    person_have = input('что у вас?')

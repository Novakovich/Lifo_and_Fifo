
def get_goods(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        goods = f.readlines()
        return goods

def get_goods_home(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        goods = f.readlines()
        return goods

STRATEGY = input('LIFO/FIFO')

while STRATEGY:
    if STRATEGY == ('FIFO'):
        goods = get_goods_home('d:/LifoAndFifo/data.txt')
        person_have = input('что у вас?')
        while goods:
            if person_have == 'exit':
                quit()
            if not person_have:
                item = goods.pop()
                i = item.split()
                print('Возьмите, вот вам', ' '.join(i))
            else:
                with open('d:/LifoAndFifo/data.txt', 'a', encoding='utf-8') as f:
                    f.writelines(['\n' + person_have])
                    print('Спасибо')
            person_have = input('что у вас?')
        STRATEGY = input('LIFO/FIFO')

    elif STRATEGY == ('LIFO'):
        person_have = input('что у вас?')
        goods = get_goods('d:/LifoAndFifo/data.txt')
        while goods:
            if person_have == 'exit':
                quit()
            if not person_have:
                item = goods.pop()
                i = item.split()
                print('Возьмите, вот вам', ' '.join(i))
            else:
                with open('d:/LifoAndFifo/data.txt', 'a', encoding='utf-8') as f:
                    f.writelines(['\n' + person_have])
            person_have = input('что у вас?')
        STRATEGY = input('LIFO/FIFO')
    elif STRATEGY == ('exit'):
        break
    else:
        STRATEGY = input('LIFO/FIFO')

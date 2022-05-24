STRATEGY = input('LIFO/FIFO')

while len(STRATEGY) >= 0:
    if STRATEGY == ('FIFO'):
        person_have = input('что у вас?')
        goods = []
        while len(goods) >= 0:
            if not person_have:
                if not len(goods):
                   print('Приходите завтра')
                   break
                else:
                   item = goods.pop()
                   print('Возьмите, вот вам', item) 
            else:
                goods.insert(0, person_have)
                print('Спасибо')
            person_have = input('что у вас?')
        STRATEGY = input('LIFO/FIFO')

    elif STRATEGY == ('LIFO'):
        person_have = input('что у вас?')
        goods = []
        while len(goods) >= 0:
            if not person_have:
                if not len(goods):
                   print('Приходите завтра')
                   break
                else:
                   item = goods.pop()
                   print('Возьмите, вот вам', item) 
            else:
                goods.append(person_have)
                print('Спасибо')
            person_have = input('что у вас?')
        STRATEGY = input('LIFO/FIFO')
    
    else:
        STRATEGY = input('LIFO/FIFO')

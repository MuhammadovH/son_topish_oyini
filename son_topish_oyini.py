# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 05:55:22 2023

@author: User
"""

def son_top(a,b):
    s=0
    import random
    tasodifiy_son=random.randint(a,b)
    print(f"Men {a}dan {b}gacha bir son o'yladim. \nUni topishga harakat qilib ko'ring!")
    while True:
        s=s+1
        mening_sonim=int(input('>>>'))
        if tasodifiy_son==mening_sonim:
            print(f'Siz men o\'ylagan sonni {s}ta urunishda topdingiz!')
            break
        else:   
            if tasodifiy_son < mening_sonim:
                print('Men o\'ylagan son bundan kichikroq!')
            else:
                print('Men o\'ylagan son bundan kattaroq!')
    return s
def son_top_pc(c,d):
    import random
    input(f'Agar {c}dan {d}gacha son  o\'ylagan bo\'lsangiz istalgan(Enter) tugmani bosing!')
    taxminlar=0
    while True:
        a=random.randint(c,d)
        taxminlar=taxminlar+1
        print(f"{a} siz o'ylgan bundan kichik bo'lsa '-', katta bo'lsa '+', \nto'g'ri bo'lsa 't' deb yozing:")
        javob=input()
        if javob=='t':
            print('Men siz o\'ylagan sonni',taxminlar,'ta urinishda topdim!')
            break
        elif javob=='+':
            c=a+1
        else:
            d=a-1
    return taxminlar
def play(e,f):
    yana = 1
    while yana == 1:
        user = son_top(e,f)
        pc = son_top_pc(e,f)
        if user > pc:
            print('Men sizni yutdim!')
        elif user < pc:
            print('Siz meni yutdingiz!')
        else:
            print('Durrang!')
        yana = int(input('Yana o\'ynamoqchimisiz Ha(1):'))
# -*- coding: utf-8 -*-
import json
import random


with open('multiLastName.json', 'r', encoding='utf-8') as f:
    multiLastName = json.load(f)


while True:
    Lname = input('請輸入主角姓氏 (輸入"h"可以查看有哪些複姓可以使用) :')
    if Lname == 'h':
        for LastName in multiLastName:
            print(LastName)

        Lname = ''

    elif Lname in multiLastName or len(Lname) == 1:
        name = input('請輸入主角名字:')
        if len(name) > 2:
            print('主角名字只能在兩字內。')
            name = ''

    else:
        print('抱歉，這個名字很遺憾無法選擇')
        Lname = ''
        name = ''

    if Lname and name:
        break

mainName = '{}{}'.format(Lname, name)
print('恭喜，你的主角名字叫做{}'.format(mainName))

# @TODO
saveData = {}
saveData['MainName'] = mainName


# Save temp file
with open('temp.sav', 'w', encoding='utf-8') as f:
    json.dump(saveData, f)

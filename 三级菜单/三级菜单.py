#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# _author_ = karlmarx123

import json
with open("file","r") as f:
    menu = json.loads(f.read())

exit_flag = False

while not exit_flag:
    print('-----省列表-----')
    for province in menu:
        print(province)
    choice = input("请选择省，q退出>>>:")
    if choice in menu:
        while not exit_flag:
            print('------市列表-----')
            for city in menu[choice]:
                print("\t",city)
            choice2 = input("请选择市，b返回>>>:")
            if choice2 in menu[choice]:
                print('--------县列表------')
                while not exit_flag:
                    for country in menu[choice][choice2]:
                        print("\t\t",country)
                    choice3 = input("请选择县，b返回>>>")
                    if choice3 in menu[choice][choice2]:
                        exit_flag =True
                        print('您选择的是：%s，%s，%s' %(choice,choice2,choice3))
                    elif choice3 =="b":
                        break
                    elif choice3 =="q":
                        exit_flag =True
            if choice2 =="b":
                break
            elif choice2 == "q":
                exit_flag = True
    elif choice =="q":
        print('====退出系统=====')
        exit_flag =True
        

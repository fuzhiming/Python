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




        



'''
         for p_num,p_key in enumerate(menu.keys(),1):
            p_dict[p_num] = p_key
            print("省的编号:%d             省的名称:%s" %(p_num,p_key))
            print("***********************************")
         find_p = input("请输入你要查询的省的编号或按q退出")
         if find_p =='q':
            flag=False
         elif find_p.isdigit() and int(find_p) <= len(p_dict):
                print("\033[32;1m%s\033[0m" %(p_dict[int(find_p)]))
                province = p_dict[int(find_p)]
                while flag:
                    cities = menu[province]
                    cities_dict = {}
                    print("*****************************")
                    for c_num,city_dict in enumerate(cities,1):
                        for city in cities_dict():
                            print("市的编号:%s    市的名称: %s"  % (c_num,city))
                            cities_dict[c_num] = city
                    print("*****************************")
                    find_city_num = input("请输入你要查询的市的编号（输入q退出，输入back返回上一层):")
                    if find_city_num =="q":
                        flag = False
                    elif find_city_num =="back":
                        break
                    elif find_city_num.isdigit() and int(find_city_num) <= len(cities):
                        print("\033[22;1m%s   %s\033[0m" %(p_dict[int(find_p)],cities_dict[int(find_city_num)]))
                        while flag:
                            countries = cities[int(find_city_num)-1][cities_dict[int(find_city_num)]]
                            print("**************************")
                            for country_num,country in enumerate(countries,1):
                                print("县/区编号：%s    县/区名称:%s"  %(country_num,country))
                                print("************************")
                                find_country_num = input("请输入你要查询的县/区的编号（输入q退出，输入back返回上一层):")
                                if find_country_num =="q":
                                    flag = False
                                elif find_country_num =="back":
                                    break
                                elif find_country_num.isdigit() and int(find_country_num) <=len(countries):
                                    print("\033[1;1m%s   %s  %s\033[0m" %(p_dict[int(find_p)],cities_dict[int(find_country_num)-1]))
                                else:
                                    print("对不起，你输入的编号不对，请核对后重新输入")
                    else:
                        print("对不起，你输入的编号有误，请核对后重新输入！")
                        flag =False

         else:
                 print("对不起，你输入的编号有误，请核对后重新输入！")

'''


#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author : karlmarx123
# 读取用户列表文件user_list数据
user_list = open('user_list','r')
data = user_list.read()
user_list.close()

# 将user_list文件数据生成列表
user_str_list = data.split()

# 将用户名，密码，错误次数以字典的形式保存至user_info_list
user_info_list = []
for i in user_str_list:
    i = i.split('|')
   user_info_list.append({
        'name':i[0],
        'pwd':i[1],
        'times':i[2]
    })
    

# 退出循环标记
exit_flag = True
# 错误用户记数
flag = 0

while exit_flag and flag < 3:
    username = input('请输入用户名或q（退出）：')
    if username != 'q':
        for item in user_info_list:
            if username == item['name']:
                while int(item['times']) < 3:
                    pwd = input('请输入密码或q(退出)：')
                    if pwd == item['pwd']:
                        print('===== 登录成功 =====')
                        item['times'] = 0
                        exit_flag = False
                        break
                    elif pwd == 'q':
                        print('==== 退出系统 ====')
                        exit_flag = False
                        break
                    else:
                        print('===== 密码错误,请重新输入 =====')
                        item['times'] = int(item['times']) + 1
                else:
                    print('用户已锁定')
                    break
                break
        else:
            print('用户不存在！')
            flag += 1
            if flag >= 3:
                print('您尝试的次数过多，退出')
    else:
        a = '退出系统'
        print(a.center(30,'='))
        exit_flag = False

# 格式化用户信息
temp_user_list = []
for item in user_info_list:
    detail = '%s|%s|%s' % (item['name'], item['pwd'], item['times'])
    temp_user_list.append(detail)
temp_list = '\n'.join(temp_user_list)

f2 = open('user_list','w')
f2.write(temp_list)
f2.close()

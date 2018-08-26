#!/usr/bin/dev python
# _*_ coding:utf-8 _*_
import os
account_file='account.txt'
lock_file='lock.txt'
loginSucc =False
for i in range(3):
    username = raw_input('username').strip()
    userpwd = raw_input('userpwd').strip()
    if len(userpwd) !=0 and len(username) !=0:
        f = file(account_file)
        for line in f.readlines():
            if username == line.split()[0] and userpwd == line.split()[1]:
                print('welcome %s in my system'%(username))
                loginSucc=True
                break
        if loginSucc == True:
            break
        else:
            pass
    else:
        continue

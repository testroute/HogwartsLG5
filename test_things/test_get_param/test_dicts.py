#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_dicts.py
@Time   :   2021/4/27 16:46   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import json
import re


def test_replace_object():
    with open('replace.json') as f:
        jsonObject = str(json.load(f))
        print("jsonstr:", jsonObject)
        list1 = re.findall("{{.*?}}", jsonObject)
        print(list1)
        data = {"memberId": 10001, "loanId": 1}
        # for i in list1:
        #     key = i.strip("}").lstrip("{")
        #     try:
        #         print(data[key])
        #     except:
        #         pass


        for i in data.keys():
            print(i,data[i])
            #replace后需要替换原json
            jsonObject = jsonObject.replace("{{"+i+"}}",str(data[i]))#replace
        # print(jsonObject.replace("{{.*?}}", "wg"))
        print(jsonObject)
        f.close()
    with open("newfile.json",mode='w',encoding="utf-8")as new_f:
        new_f.write(jsonObject.replace("'",'"'))
        new_f.close()
def test_re():
    s = '1102231990xxxxxxxx'
    res = re.search(r'(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
    print(res.groupdict())
    list1=[1,2,3,1]
    tuple1 = tuple(list1)
    print(tuple1)
    print(set(tuple1).__class__)
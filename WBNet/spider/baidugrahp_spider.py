import requests
import urllib
import re
import json
import os
import shutil
import pypinyin
import io
import imghdr
from Get_name_path import *

#https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%88%98%E4%BA%A6%E8%8F%B2

key_word=''

def get_html(word,number):
    number = number*2 #
    url = 'https://image.baidu.com/search/acjson?'
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
        }
    pn = 0
    list=[]
    new_number = 0
    while new_number < number:
        param = {
            'tn': 'resultjson_com',
            'logid': '10977306948113918012',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': '',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '',#mode
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': word,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'force': '',
            'cg': '',
            'pn': str(pn),  # 从第几张开始
            'rn': '60',  # 一次最大爬取60张
            'gsm': '1e',
            '1619422136549': ''
        }
        new_number=new_number+60
        response = requests.get(url,headers=headers,params=param).text
        text = re.findall('"thumbURL":"(.*?)"',response)
        for t in text:
            list.append(t)
        pn=int(pn)+60

    return  list


def lord_graph(list,number,name,image_path):
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
        }
    n=1
    t=0
    names = pypinyin.lazy_pinyin(name)
    name = ''
    for ns in names:
        name = name + ns

    #name = '/home/camus/Desktop/WBNet/original/' + name
    name = image_path + '/' + name
    while n <= number and n <len(list)-1:
        response = requests.get(url=list[t],headers=headers)
        t=t+1
        image = response.content
        image_b = io.BytesIO(image).read()
        size = len(image_b)
        type = imghdr.what(None,h=image_b)
        if size < 160000 and type == 'jpeg':
            with open(name+'/'+ str(n)+'.jpg','wb') as f:
                f.write(response.content)
                print('图片' + str(n)+'下载完成')
                n=n+1
        else:
            print('图片大小或格式不符')
def make_dir(name,image_path):
    list = pypinyin.lazy_pinyin(name)
    name = ''
    for l in list:
        name = name + l
    #name = '/home/camus/Desktop/WBNet/original/'+name
    image_path = image_path +'/' + name

    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    if not os.path.exists(image_path):
        os.mkdir(image_path)




def baidu_main(num,name):
    #image_path = '/home/camus/Desktop/WBSystem/original' ####
    image_path = File_readPath.read('./setting/set_original_image_path.txt')
    make_dir(name,image_path)
    list=get_html(str(name),int(num))
    lord_graph(list,int(num),name,image_path)
    names = pypinyin.lazy_pinyin(name)
    return image_path + '/' + ''.join(names)

#baidu_main(5 , '王冰冰')

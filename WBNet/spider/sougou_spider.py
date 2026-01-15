import requests
import re
import os
import pypinyin
import shutil
import io
import imghdr
from Get_name_path import *

def get_html(word,number):
    number = number*2
    url='https://pic.sogou.com/napi/pc/searchList?'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49'

    }
    pn =0
    list = []
    new_number = 0
    while new_number < number:
        param={
            'mode': '1',
            'start': str(pn),
            'xml_len': '60',
            'query': word
        }
        new_number = new_number + 60
        response = requests.get(url=url,headers=headers,params=param).text
        text=re.findall('"summarytype":".*?","thumbHeight":.*?,"thumbUrl":"(.*?)",',response)
        for t in text:
            list.append(t)
        pn = int(pn)+60
    return list

def lord_graph(list,number,name,image_path):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49'
    }
    n = 1
    t=0
    names = pypinyin.lazy_pinyin(name)
    name = ''
    for ns in names:
        name = name + ns

    #name = '/home/camus/Desktop/WBNet/original/' + name
    name = image_path + '/' + name
    while n <= number and n < len(list)-1:
        response = requests.get(url=list[t],headers=headers)
        t = t+1
        image = response.content
        image_b = io.BytesIO(image).read()
        size = len(image_b)
        type = imghdr.what(None,h=image_b)
        if size < 50000 and type == 'jpeg':
            with open(name+'/'+ str(n)+'.jpg','wb') as f:
                f.write(response.content)
                print('图片' + str(n)+'下载完成')
                n=n+1
        else:
            print('图片大小或格式不符')

def make_dir(names,image_path):
    list = pypinyin.lazy_pinyin(names)
    name = ''
    for l in list:
        name = name + l

    #name = '/home/camus/Desktop/WBNet/original/'+name
    image_path = image_path + '/' + name
    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    if not os.path.exists(image_path):
        os.mkdir(image_path)

def sougo_main(num,name):
    #image_path = '/home/camus/Desktop/WBSystem/original'  ####
    image_path = File_readPath.read('./setting/set_original_image_path.txt')
    make_dir(name,image_path)
    list=get_html(str(name),int(num))
    lord_graph(list,int(num),name,image_path)
    names = pypinyin.lazy_pinyin(name)
    return image_path+'/'+''.join(names)
#sougo_main(5,'李云龙')


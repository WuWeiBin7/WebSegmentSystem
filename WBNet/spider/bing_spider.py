import requests
import re
import os
import shutil
import pypinyin
import io
import imghdr

from Get_name_path import File_readPath


def get_html(word,number):
    number = int(number)*2
    n=0
    url ='https://cn.bing.com/images/async?'
    pn=2
    list=[]
    while n<number:
        param={
            'q': word,
            'first': str(pn),
            'count': '60',
            'cw': '1177',
            'ch': '820',
            'relp': '35',
            'tsc': 'ImageBasicHover',
            'datsrc': 'I',
            'layout': 'ColumnBased',
            'mmasync': '1',
            'dgState': 'c*6_y*1632s1553s1766s1628s1874s1689_i*36_w*182',
            'IG': '4F90E6A86E4249C9913075D2EC072706',
            'SFX': '2',  #mode
            'iid': 'images.5537'
        }
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
                }

        response = requests.get(url,headers=headers,params=param).text
        text = re.findall('<img class=".*?" style=".*?" height=".*?" width=".*?" src="(.*?)\?w=.*?&amp;',response)
        for t in text:
            list.append(t)
        pn = pn + 60
        n=n+60
    return  list


def lord_graph(list,number,name,image_path):
  #多加20个链接
    headers = {
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

    while n <= number and n < len(list):
        response = requests.get(url=list[t], headers=headers)
        t = t+1
        image = response.content
        image_b = io.BytesIO(image).read()
        size = len(image_b)
        type = imghdr.what(None,h=image_b)
        if size < 50000 and type == 'jpeg':
            with open(name + '/' + str(n) + '.jpg', 'wb') as f:
                f.write(response.content)
                print('图片' + str(n) + '下载完成')
                n = n + 1
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

def bing_main(num ,name):
    #image_path = '/home/camus/Desktop/WBSystem/original'  ####
    image_path = File_readPath.read('./setting/set_original_image_path.txt')
    make_dir(name,image_path)
    list=get_html(str(name),int(num))
    lord_graph(list,int(num),name,image_path)
    names = pypinyin.lazy_pinyin(name)
    return image_path + '/' + ''.join(names)

# bing_main(5,'欧弟')
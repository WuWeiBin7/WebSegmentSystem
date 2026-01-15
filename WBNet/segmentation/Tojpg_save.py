import os
from PIL import Image

# 转换为jpg,保存在新的文件夹
def ToJpg(file_path,mdir,new_path):
    new_path = new_path + '/' + mdir  # 新地址在这
    for fileName in os.listdir(file_path):
        # print(fileName)
        newFileName = fileName[0:len(fileName)-4]+".jpg" #.png 俩个都是可以的
        #print(newFileName)
        im = Image.open(file_path+"/"+fileName)
        folder = os.path.exists(new_path)
        if not folder:
            os.makedirs(new_path)
        else:
            pass
        im.save(new_path+"/"+newFileName)
        im.save(file_path+"/"+newFileName)

#ToJpg('/home/camus/Desktop/WBSystem/original/test','test','/home/camus/Desktop/WBSystem/InOutput')

# def main(mdir):
#     #file_path = "/home/fereen/Data/learning/2-wwb/NLPR/depth"
#     file_path = "/home/camus/Desktop/WBNet/original/"+mdir
#     ToJpg(file_path,mdir)


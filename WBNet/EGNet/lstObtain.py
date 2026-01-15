import os

def lst(mdir,new_path):

    print("---------------------------------------------------------------")

    #print("例如： /home/camus/Desktop/WBNet/InOutput/pretty")
    #path = input("请输入你想处理图片的文件地址: ")
    #path = '/home/camus/Desktop/WBNet/InOutput/' + dir
    path = new_path+'/'+mdir
    #print()

    #desktop_path = "/home/camus/Desktop/WBNet/InOutput"
    #desktop_path = input("请输入图片信息保存文件的地址: ")

    file_name = mdir+'.lst'
    #file_name = input("请输入指定文件的文件(加上后缀名): ")
    #print()

    full_path = new_path + '/' + file_name # 文件地址和文件名
    #print(full_path)

    if not os.access(full_path, os.F_OK):   # 判断文件是否存在
        file = open(full_path, 'w')

        # 获取指定目录下文件的文件名，加上绝对路径，一行一行写入指定文件中
        for root, dirs, PicNameList in os.walk(path):
            #print(dirs)
            #print(PicNameList)
            for picname in PicNameList:
                full_picpath = root + '/' + picname + '\n'
                #print(root)
                #print(full_picpath)
                file.write(full_picpath)
        print()
        file.close()
    else:
        print()

#lst('test','/home/camus/Desktop/WebSegmentSystem/InOutput')


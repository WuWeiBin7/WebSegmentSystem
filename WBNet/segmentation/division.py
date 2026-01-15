import cv2
import os

def div(mdir,img_path,msk_path,result_path):  # dir
#div('banzezhishu','/home/camus/Desktop/WBSystem/original/banzezhishu','/home/camus/Desktop/WBSystem/InOutput','/home/camus/Desktop/WBSystem/result')

    #print("例如 pretty")
    #dir = input("请输入msk和img所在的文件夹名：")

    #img_path = '/home/camus/Desktop/WBNet/original/'+dir+'/'
    img_path = img_path + '/'

    #msk_path = '/home/camus/Desktop/WBNet/InOutput/' + mdir + '/'
    msk_path = msk_path + '/' + mdir + '/'

    #result_path = '/home/camus/Desktop/WBNet/result/'+mdir
    result_path = result_path + '/' + mdir
    folder = os.path.exists(result_path)
    if not folder:
        os.makedirs(result_path)
    else:
        pass
    print('结果将保存在'+result_path)

    # 原图
    for root,dirs,picnamelist in os.walk(msk_path):
        for name in picnamelist:
            #原图
            ipath = img_path+name
            img = cv2.imread(ipath)
            # 分割图
            # /home/camus/Desktop/WBNet/InOutput/pretty/ + name
            mpath = msk_path + name
            msk = cv2.imread(mpath)
            # 调整尺寸
            size_arr = img.shape
            height = size_arr[0]
            width = size_arr[1]
            #print(height,width)
            img = cv2.resize(img, (width,height))
            msk = cv2.resize(msk, (width,height))
            #cv2.imshow('img',img)

            # 图像融合
            fground1 = cv2.add(img,255-msk)
            cv2.imwrite(result_path+'/a'+name,fground1)
            #cv2.imshow('fuse_fg',255-msk)  #人物

            fground2 = cv2.add(img,msk)
            cv2.imwrite(result_path+'/b'+name,fground2)
            #cv2.imshow('fuse_bg',fground2)  #人物

#div('zxc')
#div('me','/home/camus/1ML/me','/home/camus/Desktop/WBSystem/InOutput','/home/camus/Desktop/WBSystem/result')
# cv2.waitKey()
# cv2.destroyAllWindows()





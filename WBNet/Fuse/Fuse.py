import cv2
import os
import time
from Get_name_path import *

#通过msk和img，更换img的backgrund

def poisson_fuse(back_fullpath,
                 mdir,
                 image_path,
                 msk_path,
                 fuse_result_path):


    print()
    print("******   WBNet系列    ********")
    print("------------------------------")

    #print("例如： pty")
    #mdir = input("请输入你想处理的文件夹:")

    print()
    #print("例如：纯红色背景：/home/camus/Desktop/WBNet/BG_Transf/backgound/lADPDg7mQb7w8VPNAbfNAmI_610_439.jpg_620x10000q90g.jpg")
    #back_path = input("请输入所更换的背景图的完整地址：")


    #back_path = mback_path

    #back_name = 'lADPDg7mQb7w8VPNAbfNAmI_610_439.jpg_620x10000q90g.jpg'
    #back_name = input("请输入background的文件名：")
    # back_ground
    back = cv2.imread(back_fullpath)

    # 原图
    # imge_path = '/home/camus/Desktop/WBNet/original/'+mdir


    # 分割图
    # msk_path = '/home/camus/Desktop/WBNet/InOutput/'+mdir
    msk_path = msk_path+'/'+mdir

    #结果
    # result_path = '/home/camus/Desktop/WBNet/BG_Transf/result/'+mdir+back_name[0:4]
    back_name = Dir_infor.get_dirname(back_fullpath)
    result_path = fuse_result_path+'/' + mdir + back_name[0:4]

    folder = os.path.exists(result_path)
    if not folder:
        os.makedirs(result_path)
    else:
        pass
    print('结果将保存在'+result_path)

    for root , dirs , picnamelist in os.walk(image_path):
        for name in picnamelist:
            img = cv2.imread(image_path+'/'+name) #原图
            msk = cv2.imread(msk_path+'/'+name) #分割图
            size_arr = img.shape
            height = size_arr[0]
            width = size_arr[1]
            # height = 512
            # width = 512

            # 调整尺寸
            img = cv2.resize(img, (width, height))
            msk = cv2.resize(msk, (width, height))
            back = cv2.resize(back,(width, height))
            #cv2.imshow('img',img)
            #cv2.imshow('background',back)

            # 图像融合
            fground = cv2.add(img,255-msk)
            bground = cv2.add(back,msk)
            #cv2.imshow('fuse_fg',fground)  #人物
            #cv2.imshow('fuse_bg',bground) #背景

            s1 = cv2.subtract(fground,255-msk)  #人物图
            s2 = cv2.subtract(bground,msk)      #背景图
            #cv2.imshow('s1',s1)   #融合前景 人物等等
            #cv2.imshow('s2',s2)   #融合背景 任何背景

            '---------------应用-----------------'
            #方法一： 直接合成
            # result1 = cv2.add(s1,s2)
            # cv2.imwrite(result_path + mdir + '/result' + name, result1)

            #方法二： 透明度融合
            #result2 = cv2.addWeighted(s1, 0.8, s2, 0.7, 1)
            #cv2.imwrite(result_path+ mdir + '/result2' + name, result2)

            #方法三：泊松融合

            center = (width//2 , height//2)
            #*********msk---bground

            result3 = cv2.seamlessClone(s1,s2,bground,center,cv2.NORMAL_CLONE)
            #result3 = cv2.seamlessClone(s1,s2,bground,center,cv2.MIXED_CLONE)
            #result3 = cv2.seamlessClone(s1,s2,bground,center,cv2.MONOCHROME_TRANSFER)

            cv2.imwrite(result_path+'/result3'+name,result3)

#poisson_fuse('/home/camus/Desktop/WebSegmentSystem/BG_Transf/backgound/21.jpg','test','/home/camus/Desktop/WBSystem/original/test','/home/camus/Desktop/WBSystem/InOutput','/home/camus/Desktop/WBSystem/BG_Transf/result')
#cv2.imshow('result1',result1)
#cv2.imshow('result2',result2)
#cv2.imshow('result',result3)
#cv2.waitKey()
#cv2.destroyAllWindows()

#fusemain('tuosituoyefusiji','pll.jpg')

'''
# 原图
img = Image.open('/home/camus/Desktop/WBNet/original/pretty/0b39a56b72b7de196437576e0272b0e3.jpg')
# 分割图
msk = Image.open('/home/camus/Desktop/WBNet/InOutput/pretty/0b39a56b72b7de196437576e0272b0e3.jpg')
# 图片格式调整一致
img = img.convert('RGBA')
msk = msk.convert('RGBA')
# 尺寸调整
img = img.resize((512, 512))
msk = msk.resize((512, 512))

image = Image.blend(msk, img,0.3)
image.show()
'''
'''
img = image.imread('/media/camus/Ubuntu/1_learing/dataset/RGBD_Sal/DUT-RGBD/testset/RGB/0068.jpg')
msk = image.imread('/media/camus/Ubuntu/1_learing/result/UCNet/DUT-RGBD/pre/0068.png')

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(msk)
# 图像融合显示
plt.subplot(2, 2, 3)
plt.imshow(img,alpha=0.5)
plt.imshow(msk,alpha=0.5)
plt.show()
'''
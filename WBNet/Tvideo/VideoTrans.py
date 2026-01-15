import os
import cv2
import numpy as np
'''
------------ image to video -------------
1. use result image
2. save video result
'''


def video_trans(video_name,image_result,output_video_path):

    # ------------   file path  -------------------------------------
    #output_video_path = "/home/camus/Desktop/WBNet/video/result/"
    #path = '/home/camus/Desktop/WBNet/result/'

    video_name = str(video_name)
    video_dir = output_video_path +'/' + video_name +'.mp4'
    path = image_result + '/' + video_name

    # ------------all file rename------------------------------------
    '''
    count = 1
    oring_file_list = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹)

    # 只需要文件名为a的前景图
    temp_file_list = []
    for i in oring_file_list:
        if i[0] == 'a':
            temp_file_list.append(i)
    # 照文件名中的数字大小排序
    def int_word(name):
        return int(name[1:-4])
    file_list = sorted(temp_file_list,key=int_word)
    
    
    #重命名所有的前景图，按照1到n
    for file in file_list:  # 遍历所有文件
        olddir=os.path.join(path, file)  # 原来的文件路径
        if os.path.isdir(olddir):  # 如果是文件夹则跳过
            continue
        filename=os.path.splitext(file)[0]  # 文件名
        filetype=os.path.splitext(file)[1]  # 文件扩展名
        newdir=os.path.join(path, str(count) + filetype)  # 新的文件路径
        #print(olddir)
        #print(newdir)
        os.rename(olddir, newdir)  # 重命名
        count += 1
    '''
    #----------------------------------------------------------------
    filelist = os.listdir(path)
    img = cv2.imread(path + '/' + 'a1.jpg')  #前景图命名
    #print(img.shape)  #

    fps = 24  # 视频每秒24帧
    size = (img.shape[1], img.shape[0])  # 需要转为视频的图片的尺寸

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # opencv4.0
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, size)

    for i in range(1, int(len(filelist)/2), 1):
        im_name = path + '/a' + str(i) + '.jpg'
        frame = cv2.imread(im_name)
        videoWriter.write(frame)
        #print(im_name)

    videoWriter.release()
    #print('finish')

#video_trans('nice','/home/camus/Desktop/WBSystem/result','/home/camus/Desktop/WBSystem/video/result')
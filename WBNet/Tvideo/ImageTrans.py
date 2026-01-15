import cv2
import os
'''
-------  Video to image -------------
1. new folder  
   get image
2. save original

'''
def newfolder(result_path):
    folder = os.path.exists(result_path)
    if not folder:
        os.makedirs(result_path)
    else:
        pass
    print('视频转为图像结果将保存在' + result_path)

def image_trans(full_video_name,input_viceo_path,output_image_path):  #  video_name
# image_trans('nice.mp4',
           # '/home/camus/Desktop/WBSystem/video/input/nice.mp4',  # user select
           # '/home/camus/Desktop/WBSystem/original')

#-----------------    your_path   -----------------------------------------------------

    # your_save_path = '/home/camus/Desktop/WBNet/original/'
    # input_path = '/home/camus/Desktop/WBNet/video/input/'


#------------------   new folder  ------------------------------------------------------
    full_video_name = str(full_video_name)
    save_path = output_image_path+'/'+full_video_name[:-4]
    newfolder(save_path)


#-------------------   get image    ----------------------------------------------------

    # input_path+video_name
    cap=cv2.VideoCapture(input_viceo_path) # 获取一个视频打开cap
    isOpened=cap.isOpened # 判断是否打开
    #print(isOpened)
    fps=cap.get(cv2.CAP_PROP_FPS)
    fps_count=cap.get(cv2.CAP_PROP_FRAME_COUNT)
    #print(fps)         #  1秒有多少帧
    #print(fps_count)   #  一共有多少帧/张图像
    # 获取宽度
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 获取高度
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    i=0
    while(isOpened):
        if i==fps_count:  #
            break
        else:
            i+=1
        (flag,frame)=cap.read() # 读取每一帧，一张图像flag 表明是否读取成果 frame内容
        filename = str(i)+'.jpg'
        save_file=save_path+'/'+filename
        #print(fileName)
        # flag表示是否成功读图
        if flag==True:
            # 控制质量
            cv2.imwrite(save_file,frame,[cv2.IMWRITE_JPEG_QUALITY,100])
    print('image : finish!')

#image_trans('nice.mp4','/home/camus/Desktop/WBSystem/video/input/nice.mp4','/home/camus/Desktop/WBSystem/original')
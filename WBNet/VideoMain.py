from Tvideo import *
from WBNet import wbnet
from Get_name_path import *
'''
1. new folder 
   have image
2. save original
3. WBNet
4. save WBNet result
5. videoTrans  -- egnet.result -- video.result
6. save video result
'''

def videomain(input_video_path):  #
    output_image_path = '/home/camus/Desktop/WebSegmentSystem/original'        # 视频分割图保存到WebSegmentSystem.original
    #output_video_path = '/home/camus/Desktop/WebSegmentSystem/video/result'    # 分割后视频保存路径
    output_video_path = File_readPath.read('./setting/video_sagement_outcome_path.txt')

    full_video_name = Dir_infor.get_dirname(input_video_path)

    image_trans(full_video_name,input_video_path,output_image_path)
    # image_trans('nice.mp4',
    #             '/home/camus/Desktop/WebSegmentSystem/video/input/nice.mp4',  # user select
    #             '/home/camus/Desktop/WebSegmentSystem/original')

    video_name = full_video_name[:-4]
    input_image_path = output_image_path + '/' + video_name
    #wbnet(video_name)        # wbnet('/home/camus/1ML/me')
    image_result = wbnet(input_image_path)

    video_trans(video_name,image_result,output_video_path)  # 将WebSegmentSystem.result的图像转化为video.result中的视频
    # video_trans('nice',
    #             '/home/camus/Desktop/WebSegmentSystem/result',
    #             '/home/camus/Desktop/WebSegmentSystem/video/result')

#videomain('/home/camus/Desktop/go.mp4')
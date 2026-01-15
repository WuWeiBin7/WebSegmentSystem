from Get_name_path import *
from segmentation import *

from EGNet import run
from EGNet import lstObtain
import argparse
import os


def wbnet(image_path):  ## full_path  mdir

    print('*************欢迎使用**************')
    print("-------     让我们开始吧     ------")
    print('**********************************')

    #print("例如 pretty")
    #mdir = input("请输入msk和img所在的文件夹名：")  #me

    # 取完整路径下的文件夹名
    mdir = Dir_infor.get_dirname(image_path)


    #所有图片转为jpg格式,并保存在inoutput文件夹


    msk_path = '/home/camus/Desktop/WebSegmentSystem/InOutput'  ### EGNet result path
    #msk_path = '../InOutput'
    Tojpg_save.ToJpg(image_path,mdir,msk_path)
    #    ToJpg('/home/camus/Desktop/WebSegmentSystem/original/test','test','/home/camus/Desktop/WebSegmentSystem/InOutput')

    #产生lst文件，放入EGNet输入输出文件夹
    lstObtain.lst(mdir,msk_path)
    #    lst('test', '/home/camus/Desktop/WebSegmentSystem/InOutput')


    #调用EGNet进行处理得到 msk
    vgg_path = '/home/avicii/code/Messal/weights/vgg16_20M.pth'  # 模型的初始weight，放入相应的文件地址
    resnet_path = '/home/camus/Desktop/WebSegmentSystem/WBNet/EGNet/epoch_resnet.pth'  # 同上

    parser = argparse.ArgumentParser()

    # Hyper-parameters
    parser.add_argument('--n_color', type=int, default=3)

    parser.add_argument('--cuda', type=bool, default=True)

    # Training settings
    parser.add_argument('--vgg', type=str, default=vgg_path)
    parser.add_argument('--resnet', type=str, default=resnet_path)
    parser.add_argument('--epoch', type=int, default=30)  # 12, now x3
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--test_batch_size', type=int, default=1)
    parser.add_argument('--num_thread', type=int, default=4)
    parser.add_argument('--load_bone', type=str, default='')
    # parser.add_argument('--load_branch', type=str, default='')
    parser.add_argument('--save_fold', type=str, default='./WBNet')
    # parser.add_argument('--epoch_val', type=int, default=20)
    parser.add_argument('--epoch_save', type=int, default=1)  # 2, now x3
    parser.add_argument('--epoch_show', type=int, default=1)
    parser.add_argument('--pre_trained', type=str, default=None)

    # Testing settings
    parser.add_argument('--model', type=str, default='/home/camus/Desktop/WebSegmentSystem/WBNet/EGNet/epoch_resnet.pth')  #
    parser.add_argument('--test_fold', type=str, default='./results/test')  #
    parser.add_argument('--test_mode', type=int, default=1)
    parser.add_argument('--sal_mode', type=str, default='t')
    parser.add_argument('--mdir', type=str, default=mdir)###
    parser.add_argument('--msk_path', type=str, default=msk_path)  ###

    # Misc
    parser.add_argument('--mode', type=str, default='test', choices=['train', 'test'])
    parser.add_argument('--visdom', type=bool, default=False)

    config = parser.parse_args()

    if not os.path.exists(config.save_fold): os.mkdir(config.save_fold)
    run.main(config)

    #读取 InOutput的msk 和 original的img 进行融合并保存在result
    #result_path = '/home/camus/Desktop/WebSegmentSystem/result'  #### result
    result_path = File_readPath.read('./setting/set_result_image_path.txt')

    division.div(mdir,image_path,msk_path,result_path)
    #   div('banzezhishu','/home/camus/Desktop/WebSegmentSystem/original/banzezhishu','/home/camus/Desktop/WebSegmentSystem/InOutput','/home/camus/Desktop/WWebSegmentSystem/result')

    return result_path

#wbnet('/home/camus/1ML/me')
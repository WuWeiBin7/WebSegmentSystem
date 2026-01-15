
import WBNet
from Get_name_path import *
from Fuse import *

def fusemain(back_fullpath,image_path):

    fuse_result_path = File_readPath.read('./setting/image_fuse_path.txt')
    msk_path = '/home/camus/Desktop/WebSegmentSystem/InOutput'  ### the same of wbnet

    #
    WBNet.wbnet(image_path)

    mdir = Dir_infor.get_dirname(image_path)

    Fuse.poisson_fuse(back_fullpath,mdir,image_path,msk_path,fuse_result_path)

#fusemain('/home/camus/Desktop/WebSegmentSystem/BG_Transf/backgound/me.jpg','/home/camus/Desktop/WBNet测试/original/kebi')
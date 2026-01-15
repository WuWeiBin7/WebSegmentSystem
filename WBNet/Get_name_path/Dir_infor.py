import os

# 取完整路径下的文件夹名
def get_dirname(full_path):
    dirname = os.path.basename(full_path)
    return dirname

# get_dirname('/home/camus/Desktop/WebSegmentSystem/original/test')
# input: test


# 获取文件夹名的所在路径
def get_path(full_path):
    path = os.path.dirname(full_path)
    return path

# get_path('/home/camus/Desktop/WebSegmentSystem/original/test')
# input:  /home/camus/Desktop/WebSegmentSystem/original
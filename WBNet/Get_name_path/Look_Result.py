import subprocess

def lookresult(fileflage):
    with open(fileflage) as file1:
         setPath = file1.read()
    #subprocess.call("nautilus "+setPath, shell=True)  # 卡
    subprocess.Popen("nautilus " + setPath, shell=True)  # 不卡
    #p.kill()

#lookresult('/home/camus/Desktop/WebSegmentSystem/WBNet/setting/video_sagement_outcome_path.txt')

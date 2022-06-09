import os
from sys import argv
from turtle import screensize
from tqdm import tqdm
import shutil

def copy_other(dir1,dir2):
    dir1_list = os.listdir(dir1)
    for file in tqdm(os.listdir(dir2)):
        if file in dir1_list:       #如果dir2中的文件，也存在dir1中。就复制到指定文件下
            scr=os.path.join(dir2,file)
            des=os.path.join('Y:\\DMS_POSE\\Raw_data_1119\\Camera2',file)
            shutil.copyfile(scr,des)
            
if __name__ == '__main__':
    dir1 = argv[1]
    dir2 = argv[2]
    copy_other(dir1,dir2)
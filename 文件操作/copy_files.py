
#使用if判断语句挑选dir2中的某些文件并复制到dir1下
import os
import shutil
import tqdm
from sys import argv
def copy_files(dir1,dir2):
    for file2 in tqdm(os.listdir(dir2)):
        if '_'  in file2.split("Action_")[1].split('.')[0]:
            file2_path=os.path.join(dir2,file2)
            shutil.copy(file2_path,dir1)
if __name__ == '__main__':  
    dir1 = argv[1]
    dir2=argv[2]  
    copy_files(dir1,dir2)
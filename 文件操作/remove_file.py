import os
from sys import argv
from tqdm import tqdm

def remove_other(dir1,dir2):
    list_dir1 = os.listdir(dir1)
    for file_dir2 in tqdm(os.listdir(dir2)):
        if file_dir2 not in list_dir1:     #如果文件夹2中的文件不在文件夹1中，就删除文件夹2中的文件
            file_dir2_path = os.path.join(dir2,file_dir2)
            os.remove(file_dir2_path)
            print(file_dir2)
    
if __name__ == '__main__':
    dir1 = argv[1]
    dir2 = argv[2]
    remove_other(dir1,dir2)
    
    
    
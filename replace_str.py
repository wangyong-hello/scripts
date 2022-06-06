import os
from sys import argv
from tqdm import tqdm

def main(path,old_str,new_str):
    for file in tqdm(os.listdir(path)):
        file_path = os.path.join(path,file)
        new_path = file_path.replace(old_str,new_str)
        os.rename(file_path,new_path)

if __name__ == '__main__':
    path = argv[1]
    old_str = argv[2]
    new_str = argv[3]
    main(path,old_str,new_str)

# coding:utf-8
from ast import Try
import os
'''
    为数据集生成对应的txt文件
'''

train_txt_path = '../../Data/train.txt'
train_dir = '../../Data/train/'

valid_txt_path = '../../Data/valid.txt'
valid_dir = '../../Data/valid/'


def gen_txt(txt_path, img_dir):
    f = open(txt_path, 'w')
    for path, dirs, _ in os.walk(img_dir, topdown=True):  # 获取 train文件下各文件夹名称
        for dir in dirs:
            img_dir = os.path.join(path, dir)             # 获取各类的文件夹 绝对路径
            img_list = os.listdir(img_dir)                    # 获取类别文件夹下所有png图片的路径
            for i in img_list :
                if not i.endswith('png'):         # 若不是png文件，跳过
                    continue
                label = dir
                # img_path = os.path.join(img_dir, img_list[i])
                line = path + dir + i + ' ' + label + '\n'

                #Python: os.path.join()产生的斜杠在Windows和Linux下的不同表现和解决方法
                #直接把Windows下os.path.join()生成的反斜杠（\）全部替换为斜杠（/）
                line=line.replace('\\','/')              
                
                f.write(line)
    f.close()


if __name__ == '__main__':
    gen_txt(train_txt_path, train_dir)
    gen_txt(valid_txt_path, valid_dir)
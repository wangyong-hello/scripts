#CMD下运行该代码，脚本语言
import os
import shutil

for i in range(21):
    os.mkdir("./part2_{0}".format(i))

for n in range(21):
    files=os.listdir(os.getcwd())
    for i in range(200):
        if os.path.isfile(files[i]):
            shutil.move(files[i],"./part2_{0}".format(n))
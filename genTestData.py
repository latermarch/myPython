
import os
# 文件操作，参考
# https://www.cnblogs.com/WonderHow/p/4403727.html
import base64
import json

class inputData(object):
    def __init__(self, TaskID, Paras, DataInfo):
        self.TaskID = TaskID
        self.Paras = Paras
        self.DataInfo = DataInfo

def inputDatadict(stu):
    return json.dumps(stu, default=lambda stu: stu.__dict__)

def is_img(ext):
    ext = ext.lower()
    if ext == '.jpg':
        return True
    elif ext == '.png':
        return True
    elif ext == '.jpeg':
        return True
    elif ext == '.bmp':
        return True
    else:
        return False

def getData(directory):
    alist = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    data = []
    for i in range(0, len(alist)):
        if is_img(os.path.splitext(alist[i])[1]):
            path = os.path.join(rootdir, alist[i])
            with open(path, 'rb') as f:
                imagedata = base64.b64encode(f.read())
                data.append(imagedata.decode('utf-8'))
    return data

#-----------------------------main--------------------
taskid = '12345'

datatype = 1
AlgoParam = 'FaceRecon'
# AlgoParam = 'FaceVerify'
paras = dict((['DataType', datatype], ['AlgoParam', AlgoParam]))

# 计算照片数量
rootdir = r'./testpic'#当前目录
encodetype = 1
data = getData(rootdir)
count = (len(data))  # 计算文件个数
datainfo = dict((['count', count], ['encodetype', encodetype], ['data', data]))

inputfile = inputData(taskid, paras, datainfo)

inputfile_json = inputDatadict(inputfile)
# print(inputfile_json)
with open(rootdir+r"/testData.txt", 'w') as f:
    f.write(inputfile_json)

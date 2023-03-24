import torch

model = torch.hub.load('/home/hadoop/detectproject/yolov5-master','custom',path='/home/hadoop/detectproject/yolov5-master/fire_infrared.pt',source='local')
#img = 'https://ultralytics.com/images/zidane.jpg'
#img1 = 'http://192.168.2.82:9090/yolov5-master/data/images/test/bus.jpg'
#img2 = 'http://192.168.2.82:9090/yolov5-master/data/images/test/zidane.jpg'
#img3 = 'http://tse4-mm.cn.bing.net/th/id/OIP-C.Z64d8L37Xv5VgcnrOmOt-gHaHa'
img = 'https://img1.baidu.com/it/u=3283496392,1620863626&fm=253&fmt=auto&app=138&f=JPG?w=600&h=337'
results = model(img)
results.print()
results.save()

""""
pytorch 只py                                               pt
onnxruntime-gpu cpu/nvidia gpu               onnx
tensorrt cuda                                              onnx->tensorrt
rknn npu py暂时都不研究了 后面大概率直接CPP   onnx->rknn
"""
import cv2
from eyedetected.classi import run_cls
from eyedetected.yolov5.inference import elite_infer
import os
from filepath.settings import example_img


def image_process(information, file_pathname):
    """
   这里进行不同的opencv处理方式
    """
    if information == "0":
        # 根据传入的额信息不同，来做不同的图像处理操作
        img_pth = "/home/hadoop/eme/eyedetected/del_img/"
        for filename in os.listdir(file_pathname):
            img = cv2.imread(file_pathname + '/' + filename)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            image_np = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            res_path = "/home/hadoop/eme/eyedetected/del_img/" + filename
            cv2.imwrite(res_path, image_np)
        return img_pth
    elif information == "1":
        img_fi = "/home/hadoop/eme/eyedetected/del_img/"
        return img_fi
    elif information == "2":
        pass


def image_classification(image_path):
    res = run_cls(image_path)
    return res


def object_detection(image_res, engine_type):
    res = elite_infer(engine_type, file_path=image_res)
    return res


"""
               task
                |
              vision
                |
    检测        分类      
    |           |        
    yolo       resnet   
        
"""


class TaskPipeline:

    def division(self, infor, file_path, cls_top1="50%"):

        if infor == "图像文件":
            return ["yolo", ]
        elif infor == "结论":

            if self.func_excute(["resnet", ], file_path, engine="Pytorch") > cls_top1:
                return ["opencv_process", "yolo"]

    def func_excute(self, information, file_path, engine):

        engine_model = {
            "Pytorch": ".pt",
            "ONNX": ".onnx",
            "RKNN": ".rknn",
            "Tensorrt": ".tensorrt"
        }

        for task_func in information:

            if task_func == "resnet":
                cls_res = image_classification(file_path)
                infer_cls = cls_res[0][1]
                return infer_cls


            elif task_func == "yolo":
                infer_res = object_detection(file_path, engine_model[engine])
                return infer_res

            elif task_func == "opencv_process":
                img1 = image_process("1", file_path)
                fina_res = object_detection(image_res=img1, engine_type=engine_model[engine])
                return fina_res


if __name__ == '__main__':
    image_path = example_img
    analy = TaskPipeline().division("结论", image_path)
    res = TaskPipeline().func_excute(analy, "/home/hadoop/eme/eyedetected/example_images/zidane.jpg", "Pytorch")
    print(res)

import cv2
from eyedetected.classi import run_cls
from eyedetected.yolov5.inference import *
import os
from filepath.settings import example_img
from eyedetected.opencv_preocess import *
from eyedetected.yolov5.utils.torch_utils import select_device


class DecisionTree:
    engine_model = {
        "Pytorch": ".pt",
        "ONNX": ".onnx",
        "RKNN": ".rknn",
        "TensorRT": ".engine"
    }

    pro_func = {
        "opencv01": ill_yolo,
        "people_yolo": elite_infer,
        "classification": run_cls,
        "fire_yolo": fire_infer,
    }

    def select_func(self, file_path, cls_top1="50%", engine="Pytorch", task_type="FireDetect"):
        if task_type == "FireDetect":
            cls_res = run_cls(file_path, self.engine_model[engine])
            res = cls_res[0][1]
            if res < cls_top1:
                return ["fire_yolo"]
            elif res > cls_top1:
                return ["opencv01", "fire_yolo"]
        elif task_type == "CrowdDetect":
            return ["people_yolo"]

    def execute_func(self, task_li, file_path, engine="Pytorch"):
        global fina_res
        for i in range(len(task_li)):
            file_path = self.pro_func[task_li[i]](file_path=file_path, engine=engine)

        fina_res = file_path
        return fina_res


# def func_execute(file_path, cls_top1="50%", engine_engine="Pytorch"):
#     div_res = select_func(file_path, cls_top1, engine=engine_engine)
#     # res = list(map(execute_func, div_res))
#     res = execute_func(div_res, engine=engine_engine)
#     return res
# if __name__ == "__main__":
#     per = DecisionTree()
#     img_cls = per.select_func(example_img)
#     res = per.execute_func(img_cls, example_img)
#     print(res)

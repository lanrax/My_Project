import cv2


def ill_yolo(file_path, engine="Pytorch"):
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    _, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    img = cv2.imread(file_path)
    rep = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    mask = cv2.resize(mask, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    dst = cv2.illuminationChange(rep, mask, alpha=1, beta=2)
    path = "/home/hadoop/eme/eyedetected/example_images/test.jpg"
    cv2.imwrite(path, dst)
    print("反光处理完成！")
    return path


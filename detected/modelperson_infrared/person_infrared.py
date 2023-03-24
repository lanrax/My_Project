import json
import torch
from flask import Flask, request

app = Flask(__name__)

model_11 = torch.hub.load('/home/hadoop/detectproject/yolov5-master', 'custom',
                          '/home/hadoop/detectproject/yolov5-master/person_infrared.pt', source='local')


@app.route('/detect', methods=["POST"])
def detect():
    data = request.get_data()
    if data is None or data == "":
        Ret = {
            "status": 202,
            "result": "",
        }
        return json.dumps(Ret)
    data_json = json.loads(data)
    picture_list = data_json["picture_list"]
    picture_ids = data_json["picture_id"]
    results = model_11(picture_list)
    pic_RetDate = []
    if len(picture_list) == len(picture_ids):
        for i in range(0, len(results)):
            df = results.pandas().xyxy[i]
            column = df.shape[0]
            for j in range(column):
                data = df.loc[j]
                x_min = str(data.iloc[0])
                y_min = str(data.iloc[1])
                x_max = str(data.iloc[2])
                y_max = str(data.iloc[3])
                confidence = str(data.iloc[4])
                classno = str(data.iloc[5])
                name = data.iloc[6]
                picture_name_id = picture_ids[i]
                result = {
                    "x_min": x_min,
                    "y_min": y_min,
                    "x_max": x_max,
                    "y_max": y_max,
                    "confidence": confidence,
                    "classno": classno,
                    "name": name,
                    "picture_name": picture_name_id,
                }
                pic_RetDate.append(result)
            results.print()
        Ret = {
            "status": 200,
            "result": pic_RetDate,
        }
        return json.dumps(Ret)
    Ret = {
        "status": 201,
        "result": "",
    }
    return json.dumps(Ret)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)

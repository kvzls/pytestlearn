import requests
import csv


def postRequest(lianJie, body):
    res = requests.post(lianJie, json=body)
    print(res.json())
    return res.json()


def test_csv():
    with open("D:/pycharm/PycharmProjects/pytestlearn/test_csv.csv", "r", encoding="GBK") as f:
        reader = csv.DictReader(f)  # csv.DictReader()读到的第一行数据就是键
        data = []
        for row in reader:
            data.append(row)
        return data

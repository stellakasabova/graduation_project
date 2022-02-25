import requests
from tkinter import Label
from iptcinfo3 import IPTCInfo

class Tag:
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

def getTags(path):
    subscription_key_file = open("subscription_key.txt", "r")
    subscription_key = subscription_key_file.read()
    endpoint = 'https://cvazureapi.cognitiveservices.azure.com/'
    analyze_url = endpoint + "vision/v3.2/analyze?"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params_tags = {'visualFeatures': 'Tags'}
    with open(path, 'rb') as image:
        data = image.read()

    # Connect to Computer Vision API and get tags
    response_tags = requests.post(analyze_url, headers=headers, params=params_tags, data=data)
    tags = response_tags.json()
    tag_arr = []
    for i in range(0, len(tags["tags"])):
        temp_tag = Tag(tags["tags"][i]["name"], tags["tags"][i]["confidence"])
        tag_arr.append(temp_tag)

    return tag_arr

def getTagLabels(path, frame):
    arr = getTags(path)
    tags = []

    for i in range(0, len(arr)):
        empty_label = Label(frame, text="")
        tags.append(empty_label)

    for j in range(0, len(tags)):
        tags[j].configure(text=arr[j].name)

    return tags

def addIPTCInfo(img_path):
    temp_tag_arr = []

    tag_arr = getTags(img_path)
    for t in tag_arr:
        temp_tag_arr.append(t.name)

    img_data = IPTCInfo(img_path, force=True)
    img_data['keywords'] = []
    img_data['keywords'] = temp_tag_arr
    img_data.save()

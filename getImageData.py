import json

import requests
from tkinter import Label
from iptcinfo3 import IPTCInfo
from encrypt import *

class Tag:
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

def getTags(path):
    decrypted_data = str(decryptKeys())
    decrypted_data.replace("'", '"')

    result = json.loads(decrypted_data)
    subscription_key = result["subscription"]

    with open('sas_keys.json', 'w') as file:
        file.write(decrypted_data)
        file.close()

    encryptKeys()

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
        if temp_tag.confidence > 0.5:
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

def getCaption(path):
    decrypted_data = str(decryptKeys())
    decrypted_data.replace("'", '"')

    result = json.loads(decrypted_data)
    subscription_key = result["subscription"]

    with open('sas_keys.json', 'w') as f:
        f.write(decrypted_data)
        f.close()

    encryptKeys()

    endpoint = 'https://cvazureapi.cognitiveservices.azure.com/'
    analyze_url = endpoint + "vision/v3.2/analyze?"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params_tags = {'visualFeatures': 'Description'}
    with open(path, 'rb') as image:
        data = image.read()

    # Connect to Computer Vision API and get tags
    response_captions = requests.post(analyze_url, headers=headers, params=params_tags, data=data)
    caption = response_captions.json()
    return caption["description"]["captions"][0]["text"]

def addIPTCInfo(img_path):
    temp_tag_arr = []

    tag_arr = getTags(img_path)
    for t in tag_arr:
        temp_tag_arr.append(t.name)

    img_data = IPTCInfo(img_path, force=True)
    img_data['keywords'] = []
    img_data['keywords'] = temp_tag_arr

    img_data['caption/abstract'] = []
    img_data['caption/abstract'] = [getCaption(img_path), "stock photo"]

    img_data.save()

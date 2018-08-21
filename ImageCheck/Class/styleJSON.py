import json
import os
from ImageCheck.basic_config import basicPath


missingImagestyleJSON = []

def styleJSONCheckMissingImage():
    print("==================")
    print("Style")
    print("==================")
    #Read JSON File
    with open(basicPath.JSONDirName+basicPath.JsonfilePath+basicPath.Style) as f:
        data = json.load(f)

    flag=0

    #Get Image Path and save it to array
    for img in data["contents"]:
        #img["img_src"] = "style_jpg/filename.jpg"
        #remove "style_jpg"
        imgSrc = img["source"]["img_src"].replace("style_jpg/","")
        for file in os.listdir(basicPath.StyleImage):
            if(imgSrc==file):
                flag = 1
        if flag == 0:
            print(img["source"]["img_src"])
            missingImagestyleJSON.append(img["source"]["img_src"])
        else:
            flag=0

    with open(os.path.join(basicPath.MissingDir, "styleMissing.json"), mode='w', encoding='utf-8') as f:
        json.dump(missingImagestyleJSON, f, sort_keys=True, indent=4)

import json
import os
from ImageCheck.basic_config import basicPath



def styleJSONCheckMissingImage():
    missingImagestyleJSON = []
    print("==================")
    print("Style")
    print("==================")
    #Read JSON File
    try:

        with open(basicPath.JSONDirName+basicPath.JsonfilePath+basicPath.Style) as f:
            data = json.load(f)

            flag=0

        #Get Image Path and save it to array
        for img in data["contents"]:
        #img["img_src"] = "style_jpg/filename.jpg"
        #remove "style_jpg"
            imgSrc = img["source"]["img_src"].replace("style_jpg/","")
            for file in os.listdir(basicPath.JSONDirName+basicPath.StyleImage):
                if(imgSrc==file):
                    flag = 1
            if flag == 0:
                print(img["source"]["img_src"])
                missingImagestyleJSON.append(img["source"]["img_src"])
            else:
                flag=0

<<<<<<< HEAD
        with open(os.path.join(basicPath.MissingDir+basicPath.modelName, "styleMissing.json"), mode='w+', encoding='utf-8') as f:
=======
        with open(os.path.join(basicPath.MissingDir,basicPath.Dataname)+ "/styleMissing.json", mode='w+', encoding='utf-8') as f:
>>>>>>> 6a4c83e46b6e4891cbac3f1b8bf986dc0c450675
            json.dump(missingImagestyleJSON, f, sort_keys=True, indent=4)
    except:
        pass

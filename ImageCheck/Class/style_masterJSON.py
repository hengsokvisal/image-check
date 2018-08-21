import json
import os
from ImageCheck.basic_config import basicPath
# pprint to organize print
from pprint import pprint


styleMasterMissing = []
# Find Missing Product ID Directory
def checkMissingProductID(data):

    for img in data["products"]:
        for i in img["stylings"]:
            for proId in i["items"]:
                productIDFlag = 0
                for allProductid in os.listdir(basicPath.JSONDirName+basicPath.ProductImage):
                    if (allProductid == proId["productId"]):
                        productIDFlag = 1

                if (productIDFlag == 0):
                    # Missing ProductID Dir & Image
                    print(proId["productId"]+"/"+proId["image"])
                    styleMasterMissing.append(proId["productId"]+"/"+proId["image"])
                else:
                    productIDFlag = 0

    print("TEST",len(styleMasterMissing))
    with open(os.path.join(basicPath.MissingDir,basicPath.Dataname)+ "/styleMasterMissing.json", mode='w+', encoding='utf-8') as f:
        json.dump(styleMasterMissing, f, sort_keys=True, indent=4)



# Find Missing Style Image
def checkMissingStyleImage(data):
    styleImageFlag = 0
    for img in data["products"]:
        for i in img["stylings"]:
            for file in os.listdir(basicPath.JSONDirName+basicPath.StyleImage):
                if (i["image"] == file):
                    styleImageFlag = 1
            if(styleImageFlag == 0):
                print("style_jpg/"+i["image"])
                styleMasterMissing.append("style_jpg/"+i["image"])
            else:
                styleImageFlag = 0




def styleMasterJSONCheckMissingImage():
    styleMasterMissing.clear()
    print("==================")
    print("StyleMaster")
    print("==================")
    #Read JSON File
    with open(basicPath.JSONDirName+basicPath.JsonfilePath+basicPath.Style_master) as f:
        data = json.load(f)

    checkMissingStyleImage(data)
    checkMissingProductID(data)





import json
import os
from ImageCheck.basic_config import basicPath
# pprint to organize print
from pprint import pprint

missingImageRankingJSON = []
# Check Missing Product Image
def checkProductImage(productID,imageDir,imageName):
    ProductFlag = 0

    for productImage in os.listdir(basicPath.JSONDirName+basicPath.ProductImage+"/"+os.path.join(productID,imageDir)):
        if(imageName == productImage):
            ProductFlag = 1
    if(ProductFlag == 0):
        print(imageName)
    else:
        ProductFlag = 0




# Check whether the ProductID Directory Exist
def checkProductIDExist(productID,imageDir,imageName):
    productIDFlag = 0

    for allProductid in os.listdir(basicPath.JSONDirName+basicPath.ProductImage):
        if(productID == allProductid):
            productIDFlag = 1

    if(productIDFlag == 0):
        #Missing ProductID Dir & Image
        print(productID+"/"+imageDir+"/"+imageName)
        missingImageRankingJSON.append(productID+"/"+imageDir+"/"+imageName)
    else:
        checkProductImage(productID,imageDir,imageName)
        productIDFlag = 0
    with open(os.path.join(basicPath.MissingDir,basicPath.Dataname)+ "/rankingMissing.json", mode='w+', encoding='utf-8') as f:
        json.dump(missingImageRankingJSON, f, sort_keys=True, indent=4)



# Find all gender Img Src
def getImageSource(json,gender):
    try:
        for img in json["gender"][gender]:
            imgPath = img["source"]["img_src"]
            #products/23233/images_jpg/232323.jpg
            product,productID,imageDir,imageName, = imgPath.split("/")
            checkProductIDExist(productID ,imageDir, imageName)
    except Exception as e:
        print("error: ",e)


def rankingJSONCheckMissingImage():
    missingImageRankingJSON.clear()
    print("==================")
    print("Ranking")
    print("==================")
    #Read JSON File
    try:
        with open(basicPath.JSONDirName+basicPath.JsonfilePath+basicPath.Ranking) as f:
            data = json.load(f)

        getImageSource(data,"kids")
        getImageSource(data,"women")
        getImageSource(data,"men")
    except:
        pass

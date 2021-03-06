import json
import os
from ImageCheck.basic_config import basicPath
# pprint to organize print
from pprint import pprint
import time
from pprint import pprint

missingProductJSON = []


# Find Missing Product Img & Img color in Product.json
def findMissingProduct(data):
    productFlag = 0
    pprint(data)
    for img in data["products"]["colors"]:
        #check Product img
        products, productId, productDir, imageName = img["img"].split("/")
        try:
            for productImage in os.listdir(basicPath.JSONDirName+basicPath.ProductImage + "/" + productId + "/" + productDir):
                if (imageName == productImage):
                    productFlag = 1
                    print(imageName)
            if (productFlag == 0):
                print(imageName)
                missingProductJSON.append(img["img"])
            else:
                productFlag = 0

            productFlag = 0
        #check Product Img Color
            products, productId, productDir, imageName = img["colorImg"].split("/")
            for productImage in os.listdir(basicPath.JSONDirName+basicPath.ProductImage + "/" + productId + "/" + productDir):
                if (imageName == productImage):
                    productFlag = 1
            if (productFlag == 0):
                print(img["colorImg"])
                missingProductJSON.append(img["colorImg"])
            else:
                productFlag = 0
        except:
            pass

    with open(os.path.join(basicPath.MissingDir+basicPath.modelName, "productJSONMissing.json"), mode='w+', encoding='utf-8') as f:
        json.dump(missingProductJSON, f, sort_keys=True, indent=4)










# Find Missing Styling In Product.json
def findMissingStyling(data):

    StyleFlag = 0
    for img in data["products"]["stylings"]:
        if(img["image"].startswith("style/")):
            for styleImage in os.listdir(basicPath.JSONDirName+basicPath.StyleImage):
                imgSrc = img["image"].replace("style/", "")

                if (imgSrc == styleImage):
                    StyleFlag = 1

            if (StyleFlag == 0):
                #print(img["image"])
                missingProductJSON.append(img["image"])
            else:
                StyleFlag = 0
        else:
            products , productId , productDir , imageName = img["image"].split("/")
            try:
                for productImage in os.listdir(basicPath.JSONDirName+basicPath.ProductImage+"/"+productId+"/"+productDir):
                    if (imageName == productImage):
                        StyleFlag = 1

                if (StyleFlag == 0):
                    #print(img["image"])
                    missingProductJSON.append(img["image"])
                else:
                    StyleFlag = 0
            except:
                pass





def productJSONCheckMissingImage():
    print("==================")
    print("Product")
    print("==================")
    missingProductJSON.clear()
    #Read JSON File

    for allProductImage in os.listdir(basicPath.JSONDirName+basicPath.ProductImage):

        #Prevent OS Hidden File
        try:
            for productJson in os.listdir(basicPath.JSONDirName+os.path.join(basicPath.ProductImage,allProductImage)):
                if(productJson.startswith(allProductImage)):
                    #print(productJson)
                    with open(basicPath.JSONDirName+os.path.join(basicPath.ProductImage,allProductImage)+"/"+productJson) as f:
                        data = json.load(f)
                        #findMissingStyling(data)
                        findMissingProduct(data)
        except NotADirectoryError as e:
            print("Error: ",e)


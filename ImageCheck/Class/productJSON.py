import json
import os
from ImageCheck.basic_config import basicPath
# pprint to organize print
from pprint import pprint


missingProductJSON = []




# Find Missing Product Img & Img color in Product.json
def findMissingProduct(data):

    pprint(data)
    for img in data["products"]["colors"]:
        #print(img["colorImg"])
        productFlag = 0
        #check Product img
        products, productId, productDir, imageName = img["img"].split("/")
        for productImage in os.listdir(basicPath.ProductImage + "/" + productId + "/" + productDir):
            if (img["img"] == productImage):
                productFlag = 1
        if (productFlag == 0):
            print(img["img"])
            missingProductJSON.append(img["img"])
        else:
            productFlag = 0

        productFlag = 0
        #check Product Img Color
        products, productId, productDir, imageName = img["colorImg"].split("/")
        for productImage in os.listdir(basicPath.ProductImage + "/" + productId + "/" + productDir):
            if (img["colorImg"] == productImage):
                productFlag = 1
        if (productFlag == 0):
            print(img["colorImg"])
            missingProductJSON.append(img["colorImg"])
        else:
            productFlag = 0

    with open(os.path.join(basicPath.MissingDir, "productJSONMissing.json"), mode='w', encoding='utf-8') as f:
        json.dump(missingProductJSON, f, sort_keys=True, indent=4)










# Find Missing Styling In Product.json
def findMissingStyling(data):
    StyleFlag = 0
    for img in data["products"]["stylings"]:
        if(img["image"].startswith("style_jpg/")):
            for styleImage in os.listdir(basicPath.StyleImage):
                if (img["image"] == styleImage):
                    StyleFlag = 1

            if (StyleFlag == 0):
                print(img["image"])
                missingProductJSON.append(img["image"])
            else:
                StyleFlag = 0
        else:
            products , productId , productDir , imageName = img["image"].split("/")

            for productImage in os.listdir(basicPath.ProductImage+"/"+productId+"/"+productDir):
                if (img["image"] == productImage):
                    StyleFlag = 1

            if (StyleFlag == 0):
                print(img["image"])
                missingProductJSON.append(img["image"])
            else:
                StyleFlag = 0





def productJSONCheckMissingImage():
    print("==================")
    print("Product")
    print("==================")
    #Read JSON File

    for allProductImage in os.listdir(basicPath.ProductImage):

        #Prevent OS Hidden File
        try:
            for productJson in os.listdir(os.path.join(basicPath.ProductImage,allProductImage)):
                if(productJson.startswith(allProductImage)):
                    #print(productJson)
                    with open(os.path.join(basicPath.ProductImage,allProductImage)+"/"+productJson) as f:
                        data = json.load(f)
                        findMissingStyling(data)
                        findMissingProduct(data)
        except NotADirectoryError as e:
            print("Error: ",e)


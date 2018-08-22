from .Class import guShare , rankingJSON , styleJSON , style_masterJSON , productJSON
from ImageCheck.basic_config import basicPath
import os


def main(dirName):
    try:
        os.mkdir( basicPath.MissingDir+dirName)
    except FileExistsError as e:
        pass
    basicPath.modelName = dirName
    basicPath.JSONDirName = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+os.path.join("/ImageCheck",basicPath.ModelDir)+dirName
    guShare.guShareCheckMissingImage()
    rankingJSON.rankingJSONCheckMissingImage()
    styleJSON.styleJSONCheckMissingImage()
    style_masterJSON.styleMasterJSONCheckMissingImage()
    productJSON.productJSONCheckMissingImage()

from .Class import guShare , rankingJSON , styleJSON , style_masterJSON , productJSON
from ImageCheck.basic_config import basicPath
import os


def main(dirName):
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    basicPath.Dataname = dirName
    basicPath.JSONDirName = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+os.path.join("/ImageCheck",basicPath.ModelDir)+dirName
    print(basicPath.JSONDirName,"+++dic")
    guShare.guShareCheckMissingImage()
    rankingJSON.rankingJSONCheckMissingImage()
    styleJSON.styleJSONCheckMissingImage()
    style_masterJSON.styleMasterJSONCheckMissingImage()
    productJSON.productJSONCheckMissingImage()
    
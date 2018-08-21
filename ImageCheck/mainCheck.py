from .Class import guShare , rankingJSON , styleJSON , style_masterJSON , productJSON
from ImageCheck.basic_config import basicPath
import os


def main(dirName):

    basicPath.JSONDirName = os.path.join("ImageCheck",basicPath.ModelDir)+dirName

    guShare.guShareCheckMissingImage()
    rankingJSON.rankingJSONCheckMissingImage()
    styleJSON.styleJSONCheckMissingImage()
    style_masterJSON.styleMasterJSONCheckMissingImage()
    productJSON.productJSONCheckMissingImage()
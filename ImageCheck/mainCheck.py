from .Class import guShare , rankingJSON , styleJSON , style_masterJSON , productJSON
from ImageCheck.basic_config import basicPath
import os


def main(dirName):

    # Create MissingJSON if not exist
    if (os.path.isdir(os.path.join(basicPath.MissingDir)) == False):
        os.makedirs(os.path.join(basicPath.MissingDir))

    # Create each dir for data if not exist
    if(os.path.isdir(os.path.join(basicPath.MissingDir,dirName)) == False ):
        os.makedirs(os.path.join(basicPath.MissingDir,dirName))

    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    basicPath.JSONDirName = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+os.path.join("/ImageCheck",basicPath.ModelDir)+dirName
    basicPath.Dataname = dirName

    print(basicPath.JSONDirName,"+++dic")


    guShare.guShareCheckMissingImage()
    rankingJSON.rankingJSONCheckMissingImage()
    styleJSON.styleJSONCheckMissingImage()
    style_masterJSON.styleMasterJSONCheckMissingImage()
    productJSON.productJSONCheckMissingImage()

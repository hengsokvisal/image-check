import os
class basicPath:
    #Model name
    modelName = ""

    #Dir Name
    JSONDirName = ""
    print(JSONDirName,"++++JSONDirName")

    #Json Path
    JsonfilePath = "/others"


    #gushare JSON
    GuShare = "/gushare.json"


    #ranking JSON
    Ranking = "/ranking.json"


    #style JSON
    Style = "/style.json"


    #style_master JSON
    Style_master = "/style_master.json"


    # style image DIR NAME
    StyleImage = "/style"


    # product image DIR NAME
    ProductImage = "/products"

    # Data Model Name
    Dataname = ""


    # Missing Directory
    MissingDir = os.path.join(os.getcwd(),"ImageCheck/MissingJSON/")


    # Model Dir
    ModelDir = "Model/"

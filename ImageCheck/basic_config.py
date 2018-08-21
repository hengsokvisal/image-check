import os
class basicPath:

    #Dir Name
    JSONDirName = ""


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
    StyleImage = os.path.join(os.getcwd(),JSONDirName)+"/style_jpg"


    # product image DIR NAME
    ProductImage = os.path.join(os.getcwd(),JSONDirName)+"/products"

    # Missing Directory
    MissingDir = os.path.join(os.getcwd(),"ImageCheck/MissingJSON")


    # Model Dir
    ModelDir = "Model/"
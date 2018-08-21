from django.shortcuts import render ,HttpResponse
from .helper import addDict

import json
import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
loaFile = glob.glob(BASE_DIR+"/ImageCheck/MissingJSON/*.json")

def index(request):
    add_dict = addDict()
    for i in loaFile:
        with open(i) as handle:
            json_name = i.replace(BASE_DIR+"/ImageCheck/MissingJSON/","")
            json_type = json_name.replace(".json","")
            add_dict.add(json_type,json.loads(handle.read()))
    context =  {
        'result' : add_dict
    }
    print(request.method)
    if request.method == "POST":
        context =  {
            'result' : add_dict[request.POST['json_type']],
            'type'  : request.POST['json_type']
        }
        return render(request,"detail.html",context)
   

    return render(request , "index.html",context)
    

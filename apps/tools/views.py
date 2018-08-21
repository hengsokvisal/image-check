from django.shortcuts import render ,HttpResponse
from .helper import addDict

import json
import os
import glob
from ImageCheck import  mainCheck


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
loaFile = glob.glob(BASE_DIR+"/ImageCheck/MissingJSON/*.json")

def index(request):
    context =  {}
    if request.method == "POST":
        if (request.POST['json_type'] != "result"):
            print("okay")
            context = load_json()
            context =  {
                'result' : context['result'][request.POST['json_type']],
                'type'  : request.POST['json_type']
            }
            return render(request,"detail.html",context)
        else:
            print("why")
            mainCheck.main()
            context = load_json()
            return render(request,"result.html",context)
    return render(request , "index.html",context)
    

def load_json():
    add_dict = addDict()
    
    for i in loaFile:
        try:
            with open(i) as handle:
                json_name = i.replace(BASE_DIR+"/ImageCheck/MissingJSON/","")
                json_type = json_name.replace(".json","")
                add_dict.add(json_type,json.loads(handle.read()))
        except:
            pass
    context =  {
        'result' : add_dict
    }
    return context

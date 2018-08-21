from django.shortcuts import render ,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect

from .helper import addDict

import json
import os
import glob
from ImageCheck import  mainCheck


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def index(request):
    context =  {}
    if not request.user.is_authenticated:
        return render(request,"login.html")
    else:
        if request.method == "POST":
            if (request.POST['json_type'] != "result"):
                context = load_json()
                context =  {
                    'result' : context['result'][request.POST['json_type']],
                    'type'  : request.POST['json_type']
                }
                return render(request,"detail.html",context)
            else:
                mainCheck.main()
                context = load_json()
                return render(request,"result.html",context)
    return render(request , "index.html",context)
    

def load_json():
    loaFile = glob.glob(BASE_DIR+"/ImageCheck/MissingJSON/*.json")
    add_dict = addDict()
    print(loaFile)
    for file_json in loaFile:
        try:
            with open(file_json) as handle:
                json_name = file_json.replace(BASE_DIR+"/ImageCheck/MissingJSON/","")
                json_type = json_name.replace(".json","")
                add_dict.add(json_type,json.loads(handle.read()))
        except:
            pass
    context =  {
        'result' : add_dict
    }
    return context

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return render(request, 'login.html')
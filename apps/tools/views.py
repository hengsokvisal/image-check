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
            if ('check' in request.POST):
                mainCheck.main(request.POST['check'])
                context = {
                    'result' : load_json(request.POST['check']),
                    'recheck' : request.POST['check']
                }
                return render(request,"result.html",context)

            if ('json_type' and 'recheck' in request.POST):
                context = load_json(request.POST['recheck'])
                context =  {
                    'result' : context[request.POST['json_type']],
                    'type'  : request.POST['json_type']
                }
                return render(request,"detail.html",context)
            
        else:
            context = {
                'checks' : next(os.walk(BASE_DIR+"/ImageCheck/Model"))[1]
            }
    return render(request , "index.html",context)
    

def load_json(dirName):
    loaFile = glob.glob(BASE_DIR+"/ImageCheck/MissingJSON/"+dirName+"/*.json")
    add_dict = addDict()
    for file_json in loaFile:
        try:
            with open(file_json) as handle:
                json_name = file_json.replace(BASE_DIR+"/ImageCheck/MissingJSON/"+dirName+"/","")
                json_type = json_name.replace(".json","")
                add_dict.add(json_type,remove_duplicates(json.loads(handle.read())))
        except:
            pass
    
    return add_dict

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

def remove_duplicates(data_lists):
    newlist = []
    for data_list in data_lists:
       if data_list not in newlist:
           newlist.append(data_list)
    return newlist

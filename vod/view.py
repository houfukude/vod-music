from django.shortcuts import render_to_response
from django.http import HttpResponse
import subprocess
import os
    
def index(request):
    return render_to_response('index.html',locals())

def c(request):
    opt = request.GET.get('opt','')
    command = "deadbeef --"+opt
    subprocess.Popen(command,shell = True)
    return render_to_response('index.html',locals())

def nowplaying(request):
    get_title = "deadbeef --nowplaying '%a - %t -%b - %e'"
    music = subprocess.Popen(get_title,stdout = subprocess.PIPE,shell = True)
    nowplaying = music.stdout.read()
    return HttpResponse(nowplaying)

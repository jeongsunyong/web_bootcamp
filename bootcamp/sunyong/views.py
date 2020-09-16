from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import FileUpload
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#from django.conf import settings
from . import modules
import os


def index(request):
    return render(request,'sunyong/home.html')
# Create your views here.
def video_list(request):
    return render(request, 'sunyong/uploaded.html',{})

def process_vid(videoURL, title):
    #modules.readvid(videoURL)
    frames = modules.find_scenes(videoURL)
    #print(result[1][0].get_frames())
    modules.readvid(videoURL,frames,title)
    return

@login_required
def upload_video(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST, request.FILES)
        usr_name=request.POST["username"]
        vid_title=form.data['title']
        vid_file=request.FILES['vid']
        extension=os.path.splitext(str(vid_file))[-1].lower()

        video=FileUpload(username=usr_name, title=vid_title, vid=vid_file)
        video.save()

        #
        #Do Something
        videoURL='videos/'+usr_name+'/'+ vid_title + extension
        #videoURL='videos/'+usr_name+'/'+ '1' + extension
        process_vid(videoURL, vid_title)
        #

        return redirect('sunyong:video_list')
    else:
        form=UploadFileForm()
    return render(request, 'sunyong/videopage.html',{'form':form})

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import UploadFileForm
from .models import FileUpload
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from django.conf import settings
from . import modules
import glob
import os



def index(request):
    return render(request,'sunyong/home.html')
# Create your views here.
def video_list(request):
    return render(request, 'sunyong/uploaded.html',{})

def process_vid(videoURL, title):
    #modules.readvid(videoURL)
    frames = modules.find_scenes(videoURL)
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


        path_root=settings.MEDIA_ROOT
        path_root=path_root.replace('\\','/')
        videoURL=dir_path=os.path.splitext(videoURL)[0]
        tmp=glob.glob(path_root+videoURL+"/*.jpg")
        tmp=[pth.replace("\\","/") for pth in tmp]
        snapname= [pth.split('/')[-1] for pth in tmp]
        print(snapname)
        snaps=[settings.MEDIA_URL + videoURL + "/" + f for f in snapname]
        snapname= [pth.split('.')[0] for pth in snapname]
        context={
            'snaps':snaps,
        }
        return render(request, 'sunyong/uploaded.html', context)
    else:
        form=UploadFileForm()
    return render(request, 'sunyong/videopage.html',{'form':form})

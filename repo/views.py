from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import File
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
# Create your views here.

def repo(request):

    if request.method == 'POST':
        file = request.FILES["file"]

        if not File:
            messages.error(request, "no files for upload!")
        else:
            File.objects.create(
                publisher=User.objects.get(pk=request.user.id),
                file_name=file.name,
                file=file,
                pub_date=timezone.now(),
            )

    file_list = File.objects.all().order_by('pub_date')

    return render(request, 'repo/repo.html', {'file_list':file_list,'messages':messages})

from django.http import StreamingHttpResponse,FileResponse

def download(request, file_id):
    file = File.objects.get(pk=file_id)
    response = FileResponse(file.file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % file.file_name
    return response

def remove(request, file_id):
    f = File.objects.get(pk=file_id)
    f.file.delete()
    f.delete()
    return HttpResponseRedirect('/repo/')
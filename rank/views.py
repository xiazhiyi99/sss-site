from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
import os
import sys
from .models import *
from django.utils import timezone
import importlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
def dashboard(request):
    rank_list = Rank.objects.order_by('pub_date')
    for rank in rank_list:
        rank.update()
    context = {'rank_list':rank_list}
    return render(request, 'rank/index.html', context)

def rank_page(request, rank_id):
    rank = Rank.objects.get(pk=rank_id)

    if request.method == "POST":
        if request.user.is_authenticated:
            File = request.FILES.get("file", None)

            if not File:
                messages.error(request, "no files for upload!")

            else:#成功上传文件
                # 测试样例
                sys.path.append(os.path.join(BASE_DIR, "test"))
                test_utils = importlib.import_module( "test_" + str(rank_id) + ".test")
                feedback = test_utils.test(File)

                if feedback and (type(feedback) != str ):  # 评测成功 否则返回错误信息
                    messages.success(request, "upload over! Your score: " + str(feedback))

                    # 产生记录
                    Record.objects.create(
                        publisher=User.objects.get(pk=request.user.id),
                        score=feedback,
                        rank=rank,
                        pub_date=timezone.now(),
                    )
                    rank.submission += 1
                    return redirect("/rank/" + str(rank_id))
                else:
                    messages.error(request, feedback)

        else:#未登录
            messages.error(request, ' Please login first! ')

    record_list = Record.objects.filter(rank_id=rank_id)
    record_list = [(idx+1, r) for idx,r in enumerate(record_list.order_by('-score'))]


    context = {'rank':rank,
               'record_list':record_list,
               'message':messages,}
    return render(request,'rank/rank.html', context)














################# abolished
def submit_page(request, rank_id):
    rank = Rank.objects.get(pk=rank_id)
    if rank.state=='close':
        messages.error(request, "Rank Close!")
        return redirect("/rank/"+str(rank_id))

    if request.method == "POST":    # 请求方法为POST时，进行处理
        publisher_name = request.POST.get("publisher", None)
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not publisher_name:
            messages.error(request, "invalid name")
        elif not myFile:
            messages.error(request, "no files for upload!")
        else:#提交成功
            destination = open(os.path.join("C:\\Users\\Xia\\Desktop\\sss_site\\sss_site\\test\\test_"+str(rank_id), myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()

            #测试样例
            sys.path.append("C:\\Users\\Xia\\Desktop\\sss_site\\sss_site\\test")
            import importlib
            test_utils = importlib.import_module("test_"+str(rank_id)+'.test')
            feedback = test_utils.test(myFile)
            if feedback and (type(feedback) != str('')):#上传成功
                messages.success(request, "upload over! Your score: "+str(feedback))

                #产生记录
                Record.objects.create(
                    publisher = publisher_name,
                    score = feedback,
                    rank = rank,
                    pub_date = timezone.now(),
                )
                rank.submission += 1
                return redirect("/rank/"+str(rank_id))
            else:
                messages.error(request, feedback)



    context = {'message':messages,'rank':rank}
    return render(request,'rank/submit.html', context)
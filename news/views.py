from django.shortcuts import render
from .models import newsupdate , Feedback
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.http import HttpResponse



def home(request):
    user_list = newsupdate.objects.order_by('date')[1::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request,'news/home.html',context = { 'contex':user_list[0:9],'users': users })


def  Archive(request):
    query = request.GET.get('archive')
    datetimeObj = datetime.strptime(query, '%B %d, %Y')
    arch_req = newsupdate.objects.filter(only_date=datetimeObj)
    return render(request, 'news/Archive.html', context ={'contex':arch_req})


def  About(request):
    return render(request, 'news/About.html')



def Feedbac(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        feedback = Feedback(name = name, email=email, subject=subject, message=message)
        feedback.save()
        html = '''<html>
                                    <body> 
                                    <script>
                                    function myFunction() {
                                    alert('Thanks For Your Feedback');
                                    localStorage.clear();
                                    document.location = "/";
                                    }document.getElementById("demo").innerHTML =  myFunction()
                                    </script>
                                    </body>
                                    </html>
                                    '''
        return HttpResponse(html)
    return render(request, 'news/Feedback.html')



def  Contact(request):
    return render(request, 'news/Contact.html')


def Ads(request):
    return render(request, 'news/Advertise.html')

def Read_more(request, myid):
    read_max = newsupdate.objects.filter(id = myid)
    print(read_max)


    return render(request, 'news/descriptive.html',{'read_max': read_max[0]})
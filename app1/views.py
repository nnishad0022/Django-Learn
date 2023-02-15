from django.shortcuts import render
from django.http import HttpResponse
#from .models import details
from .models import stud1
# Create your views here.
def page1(request):
    return HttpResponse("HELLO WORLD")
def page2(request):
    return HttpResponse("GOOD MORNING")
def html_page(request):
    return render(request, "first.html")
def p2(request):
    str1 = "python100"
    l=["apple","orange","grapes","banana","pappaya","mango"]
    return render(request, "second.html", {'k1':str1, 'k2':l})
# def p3(request):
#     p1=details()
#     p1.name="nishad"
#     p1.age=23
#     p1.address="abc house"
#     p1.contact="9048990257"
#     p2=details()
#     p2.name = "vandhana"
#     p2.age = 20
#     p2.address = "v house"
#     p2.contact = "9845712357"
#     p3=details()
#     p3.name = "aami"
#     p3.age = 21
#     p3.address = "bis house"
#     p3.contact = "6238985258"
#     p4=details()
#     p4.name = "appu"
#     p4.age = 25
#     p4.address = "app house"
#     p4.contact = "9048907701"
#     p5=details()
#     p5.name = "achu"
#     p5.age = 27
#     p5.address = "cba villa"
#     p5.contact = "9633045544"
#     l=[p1,p2,p3,p4,p5]
#     return render(request,"table.html",{'k1':l})

def p6(request):
    if request.method == "POST":
        number1 = request.POST['num1']
        number2 = request.POST['num2']
        if 'add' in request.POST:
            result = int(number1) + int(number2)
            return render(request,"form.html", {'OUTPUT':result})
    return render(request,"form.html")
def join(request):
    if request.method=="POST":
        if request.POST.get('n') and request.POST.get('a'):
            formdata = stud1()
            formdata.name = request.POST.get('n')
            formdata.address = request.POST.get('a')
            formdata.save()
            return render(request, 'dbs.html')
    tabledata = stud1.objects.all()
    return render(request,'dbs.html',{'k1':tabledata})
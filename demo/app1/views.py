from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstExample(req):
    return HttpResponse("response")


def secondReq(req):
    return HttpResponse("<h1>responce</h1>")

def homeView(req):
    return render(req,"home.html")

def aboutView(req):
    return render(req,"about.html")

def worksView(req):
    username="Arun"
    services=["web development","SEO","Digital Marketing","Graphics Designer"]

    # works=[
    #     {"id":1,"title":"Ecommerce app","client":"Amal","price":1200},
    #     {"id":2,"title":"School Mng Ststem","client":"Vinu","price":1500},
    #     {"id":3,"title":"Inventory Management","client":"Amal","price":2200},
     # ]
    works=[]
    return render(req,"works.html",{"u_name":username,"sevice_list":services,"works":works})

def addWorksView(req):
    if req.method == "GET":
        return render(req,"addworks.html")
    elif req.method == "POST":
        title= req.POST.get('title')
        name=req.POST.get('client')
        price=req.POST.get('price')
        return HttpResponse(f"title: {title}  name:{name} price: {price}")


# def submitresponceView(req):
#     # print(req.POST)
#     title= req.POST.get('title')
#     name=req.POST.get('client')
#     price=req.POST.get('price')

#     return HttpResponse(f"title: {title}  name:{name} price: {price}")

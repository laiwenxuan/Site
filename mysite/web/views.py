from django.shortcuts import HttpResponse, redirect
from web.algorithm.predict import predict_salary
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from web.models import Occupation
from web import models

# Create your views here.

def Login(request):
    return render(request, 'login.html')
def Home(request):
    return render(request, 'home.html')


def OccupationTitle(request):
    return render(request,"occupationtitle.html")
def OccupationScore(request):
    return render(request, "occupationscore.html")


def PredictTitle(request):
    return render(request,"predicttitle.html")
def PredictSalary(request):
    if request.method == 'POST':
        city = request.POST.get("city")
        degree = request.POST.get("degree")
        experience = request.POST.get("experience")
        occupation = request.POST.get("occupation")
        welfare=request.POST.get("welfare")
        modelselect=request.POST.get("modelselect")
        result = predict_salary(city, degree, experience, occupation,welfare,modelselect)
        # result = predict_salary(city, degree, experience, occupation)
        return render(request, "result.html", {"result": result})

    if request.method == 'GET':
        return render(request, "predictsalary.html")
def PredictCompare(request):
    return render(request,"predictcompare.html")


def ClusteringTitle(request):
    return render(request,"clusteringtitle.html")
def ClusteringWelfare(request):
    return render(request, "clusteringwelfare.html")
def ClusteringAbility(request):
    return render(request, "clusteringability.html")


def OthersTitle(reuqest):
    return render(reuqest,"otherstitle.html")
def OthersCloudy(request):
    return render(request, "otherscloudy.html")
def OthersPie(request):
    return render(request, "otherspie.html")
def OthersHeat(request):
    return render(request, "othersheat.html")

def OccupationsTitle(request):
    return render(request,"occupationstitle.html")
#occupations display
def OccupationsList(request):
    occupations = models.Occupation.objects.all().order_by("id")# 获取所有招聘信息
    paginator = Paginator(occupations, 10)  # 每页显示10条招聘信息
    page_number = request.GET.get('page')  # 获取当前页码，默认为第1页
    page_obj = paginator.get_page(page_number)  # 获取当前页的招聘信息对象
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'occupationslist.html', context)
def OccupationsDetail(request, id):
    occupation = get_object_or_404(Occupation, id=id)
    return render(request, 'occupationsdetail.html', {'occupation': occupation})

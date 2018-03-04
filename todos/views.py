
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.db import IntegrityError

from .models import TodoItem
from .models import Post

class IndexView(ListView):
    model = TodoItem
def index(request):
    response = render(request,'predict/index.html')
    return response

def distribution(request):
    response=render(request,'distribution.html')
    return response

def bedroom(request):
    response=render(request,'bedroom.html')
    return response
#this is linear regression parameters, it could be updated using data_analysis.py
alpha=1049.80
bed=[0,260.60,723.23,1073.39,1447.07,2392.04,2210.47]
mon=[0,2.47,-160.27,-246.42,-32.12,0.74,62.94,-51.19,-496.41,0,-1223.19,584.59]

def predict(request,bedroom,month,distance):
    #We use linear regression to make a prediction
    #The parameters are pre-calculated in data analysis methods.
    predict=alpha+bed[bedroom-1]+mon[month-1]
    predict=round(predict,2)
    context_dict={}
    context_dict['predict']=predict
    response=render(request,'predictresult.html',context_dict)
    return response

from .forms import PredictForm, PostForm


def PredictForming(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            test=form.save(commit=False)##
            bed=test.bedroom
            mon=test.month
            dis=test.distance
            return predict(request,bed,mon,dis)
    else:
        form = PredictForm()
    return render(request,'predictform.html', {'form': form})
def timeseries(request):
    response=render(request,'timeseries.html')
    return response

def distance(request):
    response=render(request,'distance.html')
    return response

def post(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if not form.is_valid():
           return render(request,'post.html',{'form':PostForm,'errors':'no matching schools'})
        text = form.cleaned_data['text']
        p=Post.objects.create(text=text,)
        object_list=Post.objects.all()
        context['object_list']=object_list
        return render(request,'post.html',context)
    else:
        object_list=Post.objects.all()
        context['object_list']=object_list
        context['form'] = PostForm()
        return render(request,'post.html',context)

class PostView(ListView):
    model=Post
    template_name='post.html'




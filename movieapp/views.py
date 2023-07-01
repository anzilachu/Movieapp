from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm

def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    context={
        'movie':movie
    }
    return render(request,'detail.html',context)

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')

    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request, id):
    movie = Movie.objects.get(id=id)

    if request.method == 'POST':
        movie.delete()
        return redirect('/')

    return render(request, 'delete.html', {'movie': movie})

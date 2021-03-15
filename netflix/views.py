from django.shortcuts import render ,redirect
from .form import MovieForm
from.models import Movie
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def index(request):
    movies = Movie.objects.all()
    return render(request, "netflix/index.html",{
        'movies': movies
    })
@login_required    
@permission_required("netflix.view_movie")
def show(request, id):
    # law 3awza customize the login  far from laravel defult
    # if request.user.is_authenticated:
    #     return redirect("login")
    # if request.user.has_perms()
    movie = Movie.objects.get(pk=id)
    return render(request, "netflix/show.html",{
        "movie" : movie
    }) 
@login_required
def create(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        return redirect("index")
    
    return render(request,"netflix/create.html",{
        'form':form
    })
@login_required
def update(request):
    movie = Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None, request.Files or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "netflix/create.html",{
        'form' : form
    })
@login_required       
def delete(request):
    pass

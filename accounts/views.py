from django.shortcuts import render,redirect

#to take data from user and put it in form 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import UserCreationForm
def prepare_defult_permisions():
    objs = Permission.objects.filter(codename="view_movie").update(codename="show_movie")
# Create your views here.
def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        # password1 and password2 for confimation
        password = form.cleaned_data.get("password1")
        # return object user after make sure by authenticate form userdata and dbdata
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            
            #after opening session for new user and  redirect user to index 
            return redirect('index')
    return render(request, "registration/signup.html",{
        'form' : form
    })
    

        

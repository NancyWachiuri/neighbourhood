from django.shortcuts import render

# Create your views here.

from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,NeighbourHood,Business

from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm,PostForm,BusinessForm
from django.contrib import messages
from django .contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import DetailView,UpdateView
from django .contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime
# Create your views here.



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')


    context = {'form': form}
    return render(request,'accounts/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user is not None:
            login(request,user)
            return redirect('home')
            
        else:
            messages.info(request,'Username or password is inorrect')
            

    context = {}
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')





def userPage(request):
    context = {}

    return render(request,'accounts/user.html',context)



def profile(request):
    user = request.user
    user = Profile.objects.get_or_create(user= request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)                         
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user

    }

    return render(request, 'accounts/profile.html', context)



def home(request):
    posts = NeighbourHood.objects.all()
    context={"posts":posts}

    return render (request, 'index.html', context)



def viewPhoto(request,pk):
    photo = NeighbourHood.objects.get(id=pk)
    return render(request,'post_detail.html',{'photo':photo})


@login_required(login_url='login')
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= True)
            post.author = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request,'create_hood.html',{'form':form})




def search_results(request):
    if 'businessname' in request.GET and request.GET["businessname"]:
        search_term = request.GET.get("businessname")
        searched_articles = Business.search_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"categories": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})






@login_required(login_url='login')
def biznamtaa(request):
    posts = Business.objects.all()
    context={"posts":posts}

    return render (request, 'bizhome.html', context)




@login_required(login_url='login')
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('umash')
    else:
        form = BusinessForm()
    return render(request,'business.html',{'form':form})





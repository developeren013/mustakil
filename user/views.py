from django.shortcuts import render,redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    """if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)

            return redirect("index")
        
        context = {
        "form" : form
        }

        return render(request, "register.html" ,context)

        
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }

        return render(request, "register.html" ,context)"""


    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.filter(username = username).first()

        if user:
            messages.info(request, "Bu kullanıcı adı ile kayıtlı biri var.")
            return redirect("user:register")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.email = email
        newUser.save()
        messages.success(request, "Başarıyla kayıt oldunuz.")

        login(request,newUser)

        return redirect("index")
    context = {
            "form" : form
    }

    return render(request, "register.html" ,context)




def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı.")
            return render(request, "login.html", context)

        messages.success(request, "Başarıyla giriş yaptınız.")
        login(request,user)
        return redirect("index")

    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız")

    return redirect("index")

@login_required(login_url = "user:login")
def change_password(request):
    form = ChangePasswordForm(request.POST or None)   
    context = {
        "form": form
    }

    if form.is_valid():
        user = User.objects.get(username__exact=request.user.username)
        username = user.username
        old_pass = form.cleaned_data.get("old_pass")
        new_pass = form.cleaned_data.get("new_pass")

        user = authenticate(username = username, password = old_pass)

        if user is None:
            messages.info(request, "Şifre Yanlış")
            return render(request, "change_password.html", context)

        messages.success(request, "Şifreniz başarı ile değişti.")
        user.set_password(new_pass)
        user.save()
        login(request, user)
        return redirect("index")

    return render(request, "change_password.html", context)






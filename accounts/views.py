from django.shortcuts import render, redirect
from django.views import View
from . forms import CustomForms, UserLogInForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from . models import CustomUser
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import get_object_or_404



# Create your views here.

class Home(View):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"hello": "hello class base views"})
    
    def post(self, request, *args, **kwargs):
        pass


class Registration(View):
    print("registra===============")
    template_name = "register.html"
    form_class = CustomForms
    
    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        return render(request, self.template_name, {"form":forms})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False) 
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            image = form.cleaned_data.get('image')
            print('image===', image)
            
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username is already in used.')
                return render(request, self.template_name, {"form": form})
            
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'email is already in used.')
                return render(request, self.template_name, {"form": form})

             
            user.set_password(password) 
            user.save()

          
            authenticated_user = authenticate(request, username=username, password=password)
            print('Authenticated user:', authenticated_user)

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home') 
            else:
                print("Authentication failed")
        else:
            print('Form is invalid:', form.errors)
        return render(request, self.template_name, {"form": form})

class ProfileViews(ListView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name = 'profile'
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = CustomUser.objects.filter(id=self.request.user.id)   
        profile = get_object_or_404(queryset)
        return profile
       

     


class LoginViews(View):
    print("Login==")
    template_name = 'login.html'
    print("login===")
    form_class = UserLogInForm
    print("login====")
    
    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        return render(request, self.template_name, {'forms':forms})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
        else:
            return redirect('login')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')



    
    
    
                    
            


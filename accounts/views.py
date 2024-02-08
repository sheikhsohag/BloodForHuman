from django.shortcuts import render, redirect
from django.views import View
from . forms import CustomForms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from . models import CustomUser
from django.contrib import messages



# Create your views here.

class Home(View):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"hello": "hello class base views"})
    
    def post(self, request, *args, **kwargs):
        pass


class Registration(View):
    template_name = "register.html"
    form_class = CustomForms
    
    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        return render(request, self.template_name, {"form":forms})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            if CustomUser.objects.filter(username=username).exists:
                messages.error(request, 'Username is already in used.')
                return render(request, self.template_name, {"form": form})
            
            if CustomUser.objects.filter(email=email).exists:
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
                    
            


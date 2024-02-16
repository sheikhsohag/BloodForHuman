from django.shortcuts import render, redirect
from django.views import View
from . forms import CustomForms, UserLogInForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from . models import CustomUser
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.shortcuts import get_object_or_404



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
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print('=====================password', password)

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username is already in use.')
                return render(request, self.template_name, {"form": form})

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use.')
                return render(request, self.template_name, {"form": form})

            user = form.save(commit=False)
            user.set_password(password) 
            user.save()

            # Set location_track
            location_track = ""
            if user.district:
                location_track += user.district
            if user.subdistrict:
                location_track += " " + user.subdistrict
            if user.union:
                location_track += " " + user.union
            user.location_track = location_track
            user.save()

            authenticated_user = authenticate(request, username=username, password=password)
            print("===ok==", username, password)
            print("user==========__________+++++++++++", user, authenticated_user)
            if authenticated_user is not None:
                print("===here i am=====")
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
   
    template_name = 'login.html'
  
    form_class = UserLogInForm
   
    
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
    
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "profileUpdate.html"
    model = CustomUser
    form_class = CustomForms
    success_url = reverse_lazy('profile')  
    


    def form_valid(self, form):
        instance = form.save(commit=False)
        # Hash the password if it's being updated
        if 'password' in form.changed_data:
            instance.set_password(form.cleaned_data['password'])
        instance.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        flag=0
        pk1=None
        if form.is_valid():
            flag=1
            pk1= self.request.user.pk
            user = form.save(commit=False) 
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            image = form.cleaned_data.get('image')
            print("=======image====", image)
            
            if CustomUser.objects.exclude(id=user.id).filter(username=username).exists():
                messages.error(request, 'Username is already in use.')
                return render(request, self.template_name, {"form": form})
            
            if CustomUser.objects.exclude(id=user.id).filter(email=email).exists():
                messages.error(request, 'Email is already in use.')
                return render(request, self.template_name, {"form": form})

            if password:
                user.set_password(password)
            user.save()
            
            print(user.image)
            
            if image:  # Check if a new image is provided
                print("====in image===", image)
                user.image = image  # Update the user's image
                user.save()  # Save the user after updating the image
                print('+++++', user.image.url)
            
            location_track = ""
            if user.district:
                location_track += user.district
            if user.subdistrict:
                location_track += " " + user.subdistrict
            if user.union:
                location_track += " " + user.union
            user.location_track = location_track
            user.save()

            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('profile', pk=request.user.pk)
            else:
                messages.error(request, 'Authentication failed')
        else:
            messages.error(request, 'Form is invalid')
        return redirect('profile', pk=request.user.pk)
    

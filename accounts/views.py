from django.shortcuts import render
from django.views import View
from . forms import CustomForms


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
        pass

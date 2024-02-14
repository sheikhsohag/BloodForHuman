from django.shortcuts import render
from django.views import View
from accounts.models import CustomUser

class BloodViews(View):
    template_name = "bloodlist.html"
    model = CustomUser
    
    def get(self, request, *args, **kwargs):
        group = kwargs.get('group')
        availablelist = CustomUser.objects.filter(bloodgroup=group)
        
        return render(request, self.template_name,{'availablelist':availablelist})

class DonerDetails(View):
    template_name = "donerDetails.html"
    model = CustomUser
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        Doner = CustomUser.objects.get(id=pk)
        
        return render(request, self.template_name,{'Doner':Doner})
    
    
    
    


from django.shortcuts import render, redirect
from django.views import View
from accounts.models import CustomUser
import re
from  django.db.models import Q
from django.core.mail import send_mail 
from django.conf import settings

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


class SearchDonorView(View):
    template_name = "bloodlist.html"
    
    def post(self, request):
        blood_group = request.POST.get('blood_group')
        location = request.POST.get('location')

        donors = CustomUser.objects.all()
        if blood_group:
            donors = donors.filter(bloodgroup=blood_group)
            
        donors = donors.filter(donateStatus=True)
        
        for donor in donors:
            print(donor)
            
        if location:
            donors = donors.filter(location_track__icontains=location)
        
        return render(request, self.template_name, {'availablelist': donors})

class SearchBarDonorView(View):
    template_name = "bloodlist.html"
    
    def post(self, request):
        blood_group = request.POST.get('bloodgroup')
        location = request.POST.get('location')
        

        donors = CustomUser.objects.all()
        if blood_group:
            donors = donors.filter(bloodgroup=blood_group)
        donors = donors.filter(donateStatus=True)
        
        for donor in donors:
            print(donor)
            
        if location:
            if location:
                donors = donors.filter(location_track__icontains=location)

        
        return render(request, self.template_name, {'availablelist': donors})

    def get(self, request):
        donors = CustomUser.objects.all()
        return render(request, self.template_name, {'availablelist': donors})

# class send_Email_donor(View):
#     print("ok============ok================")
#     print("===ok==")
#     subject = "first"
#     message = "message"
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list  = [ "sheikhsohag000@gmail.com"]
#     send_mail(subject, message, from_email, recipient_list)

#     print("ok dome")

#     def post(self, request):
#         print("=====")
#         subject = "first"
#         message = "message"
#         from_email = ["sohag@gmail.com"]
#         recipient_list  = [ "sheikhsohag000@gmail.com"]
#         send_mail(subject, message, from_email, recipient_list)
#         return redirect("home")


        




    
    
    
    
    
    


from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from.forms import RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
# Create your views here.
#class Mhome(View):
 #   def get(self,request):
  #       return render(request,"arr.html")
class Mhome(TemplateView):
  template_name="arr.html"

#class RegAuth(View):
 #   def get(self,request,*args,**kwargs):
  #    f=RegistrationForm()
   #   return render(request,"registration.html",{"form":f})   
    #def post(self,request,*args,**kwargs):
     #   f=RegistrationForm(data=request.POST)
      #  if f.is_valid():
       #     f.save()
       #     messages.success(request,"user registered successfully")
        #    return redirect("h")
        #else:
         #   messages.error(request,"registration failed!..")  
          #  return render(request,"regauth.html",{"form":f})
class RegAuth(CreateView):
  form_class=RegistrationForm
  template_name="registration.html"
  model=User
  success_url=reverse_lazy("h")
  def form_valid(self, form):
    mail=form.cleaned_data.get("email")
    send_mail(
        "Around Me Registration",
        "Welcome to Around Me!!",
        "anjussajan955089@gmail.com",
        [mail]

    )
    messages.success(self.request,"registration completed")
    self.object=form.save()
    return super().form_valid(form)
  





#class LogAuth(View):
 # def get(self,request):
  #  user=request.user
   # f=LoginForm()
    #return render(request,"login.html",{"form":f,"data":user})
 # def post(self,request,*args,**kwargs):
 #  form_data=LoginForm(data=request.POST)
 #  if form_data.is_valid():
 #  un=form_data.cleaned_data.get("username")
 #  pw=form_data.cleaned_data.get("password")
 #  user=authenticate(request,username=un,password=pw)
 #  if user:
        
      #  login(request,user)
     #   messages.success(request,"login successfull")
    #    return redirect("usehome.html")
   #   else:
  #      messages.error(request,"login failed!! username or password  incorrect")
     #     return render(request,"logauth.html",{"form":form_data})   
  #    else:
    #    messages.error(request,"login failed!!")
 #       messages.error(request,"login failed!!")

#      return render(request,"logauth.html",{"form":form_data})    


class LogAuth(FormView):
  template_name="login.html"
  form_class=LoginForm
 
  def post(self,request,*args,**kwargs):
   form_data=LoginForm(data=request.POST)
   if form_data.is_valid():
     un=form_data.cleaned_data.get("username")
     pw=form_data.cleaned_data.get("password")
     user=authenticate(request,username=un,password=pw)
     if user: 
      login(request,user)
      messages.success(request,"login successfull")
      return redirect("uh")
     else:
      messages.error(request,"login failed!! username or password  incorrect")
      return render(request,"login.html",{"form":form_data})   
   else:
    messages.error(request,"login failed!!")
    return render(request,"login.html",{"form":form_data})  
   
class LogOut(View):
  def get(self,request):
    logout(request)
    return redirect("logauth")   
 
   


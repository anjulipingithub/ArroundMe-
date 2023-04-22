from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from .forms import BioForm,PChangeForm,PostForm,CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from .models import Bio,Posts,Comments

# Create your views here.
class uhome(CreateView):
    template_name="usehome.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("uh")
    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"post uploaded")
        self.objects=form.save()
        return super().form_valid(form) 
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        context["data"]=Posts.objects.all().order_by("-datetime")
        context['cform']=CommentForm()
        context['comments']=Comments.objects.all()
        return context
def addcomment(request,*args,**kwargs):
    if request.method=="POST":
       pid=kwargs.get("pid")
       post=Posts.objects.get(id=pid)
       user=request.user
       cmnt=request.POST.get("comment")
       Comments.objects.create(comment=cmnt,user=user,post=post)
       return redirect("uh") 
def addlike(request,*args,**kwargs):
    pid=kwargs.get("pid")
    post=Posts.objects.get(id=pid)
    user=request.user 
    post.likes.add(user)    
    post.save()
    return redirect("uh")      
        
class profile(TemplateView):
    template_name="profile.html"    

class BioView(CreateView):
    form_class=BioForm    
    template_name="editbio.html"
    model=Bio
    success_url=reverse_lazy("pro")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Bio Added..!!!")
        return super().form_valid(form)
    
class EditbioView(UpdateView):
    form_class=BioForm
    template_name="addbio.html"
    model=Bio
    success_url=reverse_lazy("pro")
    pk_url_kwargs="pk"
class EditPassword(FormView):
    template_name="editpass.html"
    form_class=PChangeForm
    def post(self,request,*args,**kwargs):
        form_data=PChangeForm(data=request.POST)
        if form_data.is_valid():
            current=form_data.cleaned_data.get("c_pass")
            new=form_data.cleaned_data.get("new_pass")
            confirm=form_data.cleaned_data.get("conf_pass")
            print(current)
            user=authenticate(request,username=request.user.username,password=current)
            if user:
                if new==confirm:
                    user.set_password(new)
                    user.save()
                    messages.success(request,"password changed!")
                    logout(request)
                    return redirect("logauth")
                else:
                    messages.error(request,"password mismatches!!")
                    return redirect("epas")
            else:
                messages.success(request,"Incorrect password!!")
                return redirect("epas")
        else:
            return render(request,"editpass.html",{"form":form_data})    

# class MyVlog(TemplateView):
#     template_name="myvlogs.html"
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs) 
#         user=request.
#         context["data"]=Posts.objects.filter().order_by("-datetime")
#         return context
class MyPosts(TemplateView):
    template_name="mypost.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        context['data']=Posts.objects.filter(user=self.request.user).order_by('-datetime')
        return context
    
class EditpostView(UpdateView):
    form_class=PostForm
    template_name="editpost.html"
    model=Posts
    success_url=reverse_lazy("pro")
    pk_url_kwargs="pk"

class DeletepostView(DeleteView): 
    model=Posts
    template_name="deletepost.html"
    success_url=reverse_lazy("mpost")




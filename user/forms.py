from django import forms
from.models import Bio,Posts,Comments

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
           
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "status":forms.Textarea(attrs={"class":"form-control"}),

        }  
class PChangeForm(forms.Form):  
    c_pass=forms.CharField(max_length=100,label="current password",widget=forms.PasswordInput()) 
    new_pass=forms.CharField(max_length=100,label="new password",widget=forms.PasswordInput())           
    conf_pass=forms.CharField(max_length=100,label="confirm password",widget=forms.PasswordInput())  

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts 
        fields=["image","caption"]
        widgets={
            "image":forms.FileInput(),
            "caption":forms.TextInput(attrs={"class":"form-control"}),
        }    

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]
        widgets={
            "comment":forms.Textarea(attrs={"class":"form-control"}),
        }
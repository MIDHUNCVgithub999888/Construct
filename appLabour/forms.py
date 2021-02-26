from django import forms
from .models import Sample
from .models import Images

edu=[
      

      ("SSLC","SSLC"),
      ("PLUSTWO","PLUSTWO"),
      ("DEGREE","DEGREE"),
      ("BETCH","BETCH"),
      ("OTHERS","OTHERS")
    ]
      
lang=(

    ("ENGLISH","ENGLISH"),
    ("HINDI","HINDI"),
    ("MALAYALAM","MALAYALAM")
     )
	


class RegistrationForm(forms.ModelForm):
	Password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
	ConfirmPassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
	EducationalQualification=forms.MultipleChoiceField(choices=edu,widget=forms.CheckboxSelectMultiple(choices=edu))
	LanguageKnown=forms.MultipleChoiceField(choices=lang,widget=forms.CheckboxSelectMultiple(choices=lang))
	PhoneNumber=forms.RegexField(regex=r'^\+?1?\d{10,10}$')
   
	class Meta():
		model=Sample
		fields=('Firstname','Lastname','Gender','Age','EducationalQualification','LanguageKnown','Address','Email','Photo','Village','District','Country','PhoneNumber','Password','ConfirmPassword')

class LoginForm(forms.ModelForm):
	Password=forms.CharField(widget=forms.PasswordInput)

	class Meta():
		model=Sample
		fields=('Email','Password')

class UpdateForm(forms.ModelForm):
	class Meta():
		model=Sample
		fields=('Firstname','Lastname','Gender','Age','EducationalQualification','LanguageKnown','Address','Email','Photo','Village','District','Country','PhoneNumber','Password','ConfirmPassword')
		
class PasswordChangeForm(forms.Form):
	OldPassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
	NewPassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
	ConfirmPassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)

class ImageForm(forms.ModelForm):
	class Meta():
		model=Images
		fields=('Name','Color','Price','Image','Model')

class ImageGallery(forms.ModelForm):
	class Meta():
		model=Images
		fields=('Image',)

class ProductDetailsForm(forms.ModelForm):
	class Meta():
		model=Images
		fields=('Name','Color','Price','Image','Model')
	
	
		



 		
 		



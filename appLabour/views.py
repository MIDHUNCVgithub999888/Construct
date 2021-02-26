from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import RegistrationForm,LoginForm,UpdateForm,PasswordChangeForm,ImageForm,ProductDetailsForm
from .models import Sample, Images
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
	return render(request,'index.html')
	
def UserRegistration(request):
	if request.method=="POST":
		form = RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			firstname=form.cleaned_data['Firstname']
			lastname=form.cleaned_data['Lastname']
			gender=form.cleaned_data["Gender"]
			age=form.cleaned_data['Age']
			educationalqualification=form.cleaned_data["EducationalQualification"]
			languageknown=form.cleaned_data["LanguageKnown"]
			address=form.cleaned_data['Address']
			email=form.cleaned_data['Email']
			photo=form.cleaned_data['Photo']
			village=form.cleaned_data['Village']
			district=form.cleaned_data['District']
			country=form.cleaned_data['Country']
			phonenumber=form.cleaned_data['PhoneNumber']
			password=form.cleaned_data['Password']
			confirmpassword=form.cleaned_data['ConfirmPassword']
			

			ur=Sample.objects.filter(Email=email).exists()

			if ur:
				msg="User with same EmailAddress is already exists"
				args={'form':form,'error':msg}
				return render(request,'Registration.html',args)

			elif password!=confirmpassword:
				msg="enter correct password!password mismatch"
				args={'form':form,'error':msg}
				return render(request,'Registration.html',args)

			else:
				res=Sample(Firstname=firstname,Lastname=lastname,Gender=gender,Age=age,EducationalQualification= educationalqualification,LanguageKnown=languageknown,Address=address,Email=email,Photo=photo,Village=village,District=district,Country=country,PhoneNumber=phonenumber,Password=password,ConfirmPassword=confirmpassword)
				res.save()
				return redirect('/UserRegistration')
				return HttpResponse("success")

	else:
		form=RegistrationForm()
	return render(request,'Registration.html',{'form':form})

def UserLogin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['Email']
			password = form.cleaned_data['Password']

			try:
				ur = Sample.objects.get(Email=email,Status=True)
				if not ur:
					msg="Incorrect Email or password!"
					args={'form':form,'error':msg}
					return render(request,'Login.html',args)
				elif password!=ur.Password:
					msg="Incorrect Email or Password"
					args={'form':form,'error':msg}
					return render(request,'Login.html',args)
				else:
					request.session['email'] = email
					request.session['sid'] = ur.id
					return redirect('/UserHome/%s' % ur.id)
        
			except:
				
                
				msg="Incorrect email or password"
				args={"form":form,'error':msg}
				return render(request,'Login.html',args)
	else:
		form=LoginForm()
	 	
	return render(request,'Login.html',{'form':form})

def UserHome(request,id):
	if request.session.has_key:
		email=request.session["email"]
		uid=request.session["sid"]
		user=Sample.objects.get(id=id)
		ur=Sample.objects.get(Email=email)
		return render(request,'Home.html',{'ur':ur,'user':user})

def ViewProfile(request,id):
	user=Sample.objects.get(id=id)
	if request.method=='POST':
		form=UpdateForm(request.POST,instance=user)
		if form.is_valid():
			form.save()
			return redirect('/UserHome/%s' % user.id)
	return render(request,'Profile.html',{'user':user})

def UserDelete(request,id):
	user=Sample.objects.get(id=id)
	user.delete()
	return redirect("/index")

def UserLogout(request):
	# logout(request)
	messages.info(request,'logout successfully...')
	return redirect('/index')

def ChangePassword(request,id):
	uid=request.session['sid']
	user=Sample.objects.get(id=id)
	if request.method=='POST':
		form=PasswordChangeForm(request.POST)
		if form .is_valid():
			oldpassword=form.cleaned_data["OldPassword"]
			newpassword=form.cleaned_data["NewPassword"]
			confirmpassword=form.cleaned_data["ConfirmPassword"]
			if oldpassword!=user.Password:
				msg='enter the correct password'
				return render(request,'ChangePassword.html',{'form':form,'error':msg,'user':user})
			elif newpassword!=confirmpassword:
				msg="password does not match"
				return render(request,'ChangePassword.html',{'form':form,'error':msg,'user':user})
			else:
				user.Password=newpassword
				user.ConfirmPassword=confirmpassword
				user.save()
				msg="Password ChangePassword successfully"
				return redirect('UserHome/%s' %id)
				return render(request,'ChangePassword.html',{'form':form,'error':msg,'user':user})
	else:
		form=PasswordChangeForm()

	return render(request,'ChangePassword.html',{'form':form,'user':user})

def ImageUpload(request):
	if request.method == 'POST':
		form=ImageForm(request.POST, request.FILES)
		if form.is_valid():
			Name=form.cleaned_data['Name']
			Color=form.cleaned_data['Color']
			Price=form.cleaned_data["Price"]
			Image=form.cleaned_data['Image']
			Model=form.cleaned_data['Model']
			form.save()
			return redirect('/index')
			return render(request,'ImageUpload.html',{'form':form})

	else:
		form=ImageForm()
	return render(request,'ImageUpload.html',{'form':form})

def ImageGallery(request):
	image=Images.objects.all()

	return render(request,'ImageGallery.html',{'image':image})


def ProductDetails(request,pk):
	image=Images.objects.get(id=pk)
	return render(request,'Details.html',{'image':image})

def View_404(request):
	user=Sample.objects.all()
	return redirect("/index")
	
		
	


	




	
	
	
		
		
	






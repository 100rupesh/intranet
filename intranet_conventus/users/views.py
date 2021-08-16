from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

#Signup View
@login_required(login_url='/users/login/')
def signup(request):
	if request.method=='POST':
		fm=UserCreationForm(request.POST)
		
		if fm.is_valid():
			fm.save()
			return redirect('/')
	else:
		fm=UserCreationForm()
	return render(request,'users/signup.html',{'form':fm})


#Login View

def user_login(request):
	if request.method=='POST':
		fm=AuthenticationForm(request=request,data=request.POST)
		if fm.is_valid():
			uname=fm.cleaned_data['username']
			upass=fm.cleaned_data['password']
			user=authenticate(username=uname,password=upass)
			if user is not None:
				
				request.session['userId']=user.id
				request.session['userName']=uname
				login(request,user)

				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
				else:	
					return HttpResponseRedirect('/')
	else:			
		fm=AuthenticationForm()
	return render(request,'users/login.html',{'form':fm})


def user_logout(request):
	logout(request)
	return redirect('/users/login/')



def changepassword(request):
    if request.method=='POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/users/login/')

    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'users/changepass.html',{'form':fm})


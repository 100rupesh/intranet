#this is a views file
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
import datetime
from django.views.generic import *
from .forms import *

# Create your views here.
def index(request):
	return render(request,'events/index.html')


def holiday(request):
	h=Holiday.objects.all()

	return render(request,'events/holiday.html',{'x':h})


def conveyance(request):
	if request.method == 'GET':

	
	
		return render(request,'events/conveyance.html')
	else:
		user=(request.session.get('userId'))
		date=(datetime.datetime.now())
		Cdate=(request.POST.get('cdate'))
		from_loc=request.POST.get('from')
		to_loc=request.POST.get('to')
		amount=int(request.POST.get('amount'))
		remark=request.POST.get('remark')
		conveyance=Conveyance(Date=date,From_Location=from_loc,To_Location=to_loc,Conveyance_Date=Cdate,user=User(id=user),Amount=(amount),Remark=remark)
		conveyance.save()
		return redirect("/conveyancelist/")


	


def conveyancelist(request):
    uid=request.session.get('userId')
    incl=Conveyance.objects.filter(user_id=uid).order_by('-Date')
    d={'x':incl}
    return render(request,'events/conveyancelist.html',d)



def allconveyancelist(request):
	if request.user.username == 'admin':
	    u=Conveyance.objects.all().order_by('-Date')

	    return render(request,'events/allconveyancelist.html',{'x':u})
	else:
		return HttpResponse("You arent Allowed Here !")




class Conveyanceupdateview(UpdateView):
    model=Conveyance
    template_name='events/updateconveyance.html'
    fields=('Status','RemarkAdmin')
    success_url='/allconveyancelist/'


class Conveyanceupdateviewuser(UpdateView):

    model=Conveyance
    template_name='events/updateconveyanceuser.html'
    fields=('From_Location','To_Location','Conveyance_Date','Remark','image')
    success_url='/conveyancelist/'



def holidayform(request):
	if request.method=="GET":
		return render(request,'events/holidayform.html')
	else:
		date=(request.POST.get('hdate'))
		day=(request.POST.get('hday'))
		occasion=(request.POST.get('occasion'))
		print(occasion,date,day)
		holiday=Holiday(Date=date,Day=day,Occasion=occasion)
		holiday.save()
		return redirect("/holiday/")


def deleteview(request,id):
	c=Conveyance.objects.get(id=id)
	c.delete()
	return redirect('/allconveyancelist/')

def editholiday(request):
	holiday=Holiday.objects.all()

	return render(request,'events/editholiday.html',{'x':holiday})


class holidayedit(UpdateView):

    model=Holiday
    template_name='events/holidayedit.html'
    fields=('Date','Day','Occasion')
    success_url='/holiday/'


def deleteholiday(request,id):
	c=Holiday.objects.get(id=id)
	c.delete()
	return redirect('/holiday/')


def Post(request):
     if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

        
            

     else:
        form=PostForm()
        return render(request,'events/post.html',{'form':form})



def Notice(request):
     if request.method == 'POST':
        form=NoticeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

        
            

     else:
        form=NoticeForm()
        return render(request,'events/notice.html',{'form':form})


def postview(request):
	po=Post.objects.all()
	return render(request,'events/postview.html',{'x':po})
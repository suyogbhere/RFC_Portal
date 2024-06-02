from django.shortcuts import render, HttpResponseRedirect
from myapp.forms import *
from myapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,update_session_auth_hash, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request,'myapp/dashboard.html',locals())


def user_login(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass= fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user.is_staff:
                login(request,user)
                messages.success(request,'log in successfully!!!')
                return HttpResponseRedirect('/home/')
            else:
                messages.error(request,'Something went wrong')
    else:
        fm=AuthenticationForm()
    return render(request,'myapp/rfc_login.html',locals())

def Change_Password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = MyPasswordChangeForm(user=request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Change successfully!!!')
                return HttpResponseRedirect("/login/")
            else:
                messages.error(request,'Please correct the error')
                return HttpResponseRedirect('/cp/')
        else:
            fm = MyPasswordChangeForm(user=request.user, label_suffix='')
        return render(request,'myapp/password_change.html',{'form':fm, 'CP':'active'})
    else:
        return HttpResponseRedirect("/login/")


def Raise_Rfc(request):
    if request.method == 'POST':
        form = RFC_Raised_Form(request.POST,request.FILES)
        if form.is_valid():
            rfn=form.cleaned_data['Reference_RFC_No']
            dpt=form.cleaned_data['Department']
            rt=form.cleaned_data['Request_Type']
            env=form.cleaned_data['Environment']
            pd=form.cleaned_data['Planned_Date']
            cat=form.cleaned_data['Category']
            rfc=form.cleaned_data['Reason_for_change']
            doc=form.cleaned_data['Description_of_change']
            sd=form.cleaned_data['System_Details']
            tbeb=form.cleaned_data['To_be_executed_by']
            crb=form.cleaned_data['Change_Requested_by']
            ca=form.cleaned_data['Change_authorizer']
            cl=form.cleaned_data['Change_level']
            cia=form.cleaned_data['Change_impact_assessment']
            rr=form.cleaned_data['Risk_Rating']
            att=form.cleaned_data['Attachments']
            crf=form.cleaned_data['Change_rollback_procedures']
            data=RFC_Register(Reference_RFC_No=rfn,Department=dpt,Request_Type=rt,Environment=env,Planned_Date=pd,Category=cat,Reason_for_change=rfc,Description_of_change=doc,
                          System_Details=sd,To_be_executed_by=tbeb,Change_Requested_by=crb,Change_authorizer=ca,Change_level=cl,
                          Change_impact_assessment=cia,Risk_Rating=rr,Attachments=att,Change_rollback_procedures=crf)
            print('DATA',data)
            data.save() 
            print("data saved successfully!!!")
            form = RFC_Raised_Form()
            messages.success(request,'RFC Raised succefully!!!!')
    else:
        print("request GET")
        form = RFC_Raised_Form()
        # form1 = Activity_Form()
    return render(request,'myapp/rfc_registration.html',locals())

# def View_Raise_Rfc(request,pk):
#     return render(request,'myapp/View_rfc_details.html',locals())


def Rejected_Rfc(request):
    form = RFC_Raised_Form()
    return render(request,'myapp/rejected_rfc.html',locals())


def Rollback_Rfc(request):
    form = RFC_Register.objects.all()
    return render(request,'myapp/rollback_rfc.html',locals())

def My_Rfc(request):
    all_rfc = RFC_Register.objects.all()
    return render(request,'myapp/my_rfc.html',locals())

def Rfc_details(request,pk):
    pi = RFC_Register.objects.get(Rfc_Number=pk)
    rfc = RFC_Raised_Form(instance=pi)
    return render(request,'myapp/rfc_details.html',locals())


def Opened_rfc(request):
    return render(request, 'myapp/open_rfc.html',locals())


def Closed_rfc(request):
    return render(request, 'myapp/closed_rfc.html',locals())
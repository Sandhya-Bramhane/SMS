from django.shortcuts import render
from django.http import HttpResponseRedirect
from data.models import Registration,Admin,Student,Notice,Hostel

def MyHomePage(request):
    return render(request,'home.html')

def MyLoginPage(request):
    if request.method == 'POST':
        email=request.POST['emailid']
        pass1=request.POST['pass']
        s1=Registration.objects.filter(email=email,pass1=pass1).exists()
        if(s1== True):
            print(email)
            request.session['user']=email
            user=request.session['user']=email
            print("user",user)
            return render(request,'userhome.html',{'user':user})
            #return HttpResponseRedirect('/myuser',{"key" : user})

        else:
            s2=Admin.objects.filter(email=email,pass1=pass1).exists()
            if(s2== True):
                request.session['user']=email
                user=request.session['user']=email
                print("user",user)
                return render(request,'adminhome.html',{'user':user})
    return render(request,'login.html')

def MySignUpPage(request):
    if request.method=='POST':
        un=request.POST['uname']
        email=request.POST['emailid']
        pass1=request.POST['pass']
        mob=request.POST['mobile']
        s1=Registration(name=un,email=email,pass1=pass1,mobile=mob)
        s1.save()
        return HttpResponseRedirect('/mylogin')
    return render(request,'signup.html')

def MyUserHome(request):
    return render(request,'userhome.html')

def MyAdminHome(request):
    return render(request,'adminhome.html')

def MyStudent(request):
    try:
        if request.method == 'POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            add=request.POST['add']
            gen=request.POST['gen']
            state=request.POST['state']
            city=request.POST['city']
            dob=request.POST['dob']
            course=request.POST['course']
            email=request.POST['email']
            s1=Student(sname=fname,slname=lname,sadd=add,sgen=gen,sstate=state,scity=city,sdob=dob,scor=course,semid=email)
            s1.save()
    except Exception as e1:
        print("Error=",e1)
    return render(request,'Student.html')

def MyNotice(request):
    if request.method == 'POST':
        nid=request.POST['nid']
        dt=request.POST['date1']
        sub=request.POST['sub']
        dept=request.POST['dept']
        n1=Notice(nid=nid,dt=dt,sub=sub,dept=dept)
        n1.save()
        return HttpResponseRedirect('/adminnotice')
    return render(request,'Notice.html')

def MYNoticedelete(request):
    nid=request.GET['nid']
    print("ID=",nid)
    n1=Notice.objects.get(nid=nid)
    n1.delete()
    return HttpResponseRedirect('/adminnotice')

def NoteUpdate(request):
    nid=request.GET['nid']
    n1=Notice.objects.get(nid=nid)
    dict1={

        'note':n1
    }
    return render(request,'NoticeUpdate.html',dict1)

def NoticeUpdate(request):
    try:
        if request.method == 'POST':
            nid=request.POST['nid']
            date1=request.POST['date1']
            sub=request.POST['sub']
            dept=request.POST['dept']
            n1=Notice.objects.get(nid=nid)
            n1.dt=date1
            n1.sub=sub
            n1.dept=dept
            n1.save()
    except Exception as e1:
        print("Error=",e1)
    return HttpResponseRedirect('/adminnotice')
     

def AdminNotice(request):
    n1=Notice.objects.all();
    dict1={
        'note':n1
    }
    return render(request,'adminnotice.html',dict1)

def AdminUser(request):
    s1=Student.objects.all();
    dict1={
        'data':s1
    }
    return render(request,'adminuser.html',dict1)
def AdminUserRemover(request):
    id=request.GET['id']
    s1=Student.objects.get(id=id)
    s1.delete()
    return render(request,'adminuser.html')

def AdminUserUpdate(request):
    id=request.GET['id']
    s1=Student.objects.get(id=id)
    dict1={
        'data':s1
    }
    return render(request,'adminuserupdate.html',dict1)

def StudentUpdate(request):
    try:
        if request.method == 'POST':
            id=request.POST['id']
            fname=request.POST['fname']
            lname=request.POST['lname']
            add=request.POST['add']
            gen=request.POST['gen']
            state=request.POST['state']
            city=request.POST['city']
            dob=request.POST['dob']
            course=request.POST['course']
            email=request.POST['email']
            s1=Student.objects.get(id=id)
            s1.sname=fname
            s1.slname=lname
            s1.sadd=add
            s1.sgen=gen
            s1.sstate=state
            s1.scity=city
            s1.sdob=dob
            s1.scor=course
            s1.semid=email
            s1.save()
    except Exception as e1:
        print("Error=",e1)
    return HttpResponseRedirect('/adminuser')

def MyUserNotice(request):
    n1=Notice.objects.all()
    dict1={
        'note':n1
    }
    return render(request,'usernotice.html',dict1)


# hostel addmission
def HostelAdddata(request):
    h1=Hostel.objects.all()
    dict1={
        'add':h1
    }
    return render(request,'hosteldata.html',dict1)

def HostelAdd(request):
    if request.method == 'POST':
        sid=request.POST['sid']
        dt=request.POST['dt']
        fn=request.POST['fname']
        ln=request.POST['lname']
        mo=request.POST['mobile']
        co=request.POST['course']
        dept=request.POST['depat']
        du=request.POST['dura']
        h1=Hostel(sid=sid,dt=dt,fn=fn,ln=ln,mo=mo,co=co,dept=dept,du=du,action='pending')
        h1.save()
        return HttpResponseRedirect('/hostadd')
    return render(request,'userhostel.html')

def HostelUserRemover(request):
    sid=request.GET['sid']
    print("ID=",sid)
    h1=Hostel.objects.get(sid=sid)
    h1.delete()
    return HttpResponseRedirect('/hosteldata')

def HostelUpdate(request):
    hid=request.GET['hid']
    h1=Hostel.objects.get(sid=hid)
    print(h1)
    dict1={
        'data':h1
    }
    return render(request,'hostelupdate.html',dict1)

def HostelChange(request):
    if request.method == 'POST':
        sid=request.POST['sid']
        dt=request.POST['dt']
        fn=request.POST['fname']
        ln=request.POST['lname']
        mo=request.POST['mobile']
        co=request.POST['course']
        dept=request.POST['depat']
        du=request.POST['du']
        action=request.POST['action']
        h1=Hostel.objects.get(sid=sid)
        h1.dt=dt
        h1.fn=fn
        h1.ln=ln
        h1.mo=mo
        h1.co=co
        h1.dept=dept
        h1.du=du
        h1.action=action
        h1.save()
        return HttpResponseRedirect('/myadmin')
    return render(request,'userhostel.html')

def UserHostelData(request):
    h1=Hostel.objects.all()
    dict1={
        'add':h1
    }
    return render(request,'userhosteldata.html',dict1)
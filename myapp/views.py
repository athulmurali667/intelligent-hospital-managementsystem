from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return  render(request,"index.html")

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']

    ob1 = login_table.objects.filter(username=username, password=password).exists()
    if ob1:
        try:
            ob=login_table.objects.get(username=username,password=password)
            request.session["lid"] = ob.id
            if ob.type=='admin':
                return HttpResponse('''<script>alert("success");window.location="/adminhome"</script>''')
            elif ob.type=='hospital':
                return HttpResponse('''<script>alert("success");window.location="/hospitalhome"</script>''')
            elif ob.type=='doctor':
                return HttpResponse('''<script>alert("success");window.location="/DoctorHome"</script>''')
            elif ob.type=='user':
                return HttpResponse('''<script>alert("success");window.location="/userhome"</script>''')
            else:
                return HttpResponse('''<script>alert("invaild");window.location="/"</script>''')

        except:
            return HttpResponse('''<script>alert("invaild error occurs");window.location="/"</script>''')


    else:
        return HttpResponse('''<script>alert("invaild user");window.location="/"</script>''')


def adddep(request):
    return  render(request,"admin/Add_depatments.html")

def addep_post(request):
    depname=request.POST['textfield']
    depdetails=request.POST['textfield2']
    ob=department_table()
    ob.department=depname
    ob.details=depdetails
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location="/ManageDepartment"</script>''')
def deletedepartment(request,id):
    ob=department_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/ManageDepartment"</script>''')


def adminhome(request):
    return render(request,"admin/adminindex.html")

# def viewpatient(request):
#     ob = hospital_table.objects.all()
#     return render(request, "admin/admin_view_verified_hospital.html", {"val": ob})





def changepassword(request):
    return render(request,"admin/ChangePassword.html")

def changepassword_post(request):
     cpassword=request.POST['currentpassword']
     newpassword=request.POST['Newpassword']
     conpassword=request.POST['Confirmpassword']
     ob=login_table.objects.get(id=request.session['lid'])
     if ob.password == cpassword:
         if  newpassword==conpassword:
             ob.password=conpassword
             ob.save()
             return HttpResponse('''<script>alert("password changed");window.location="/changepassword"</script>''')
         else:
             return HttpResponse('''<script>alert("new password is not equal to conform password");window.location="/changepassword"</script>''')
     else:
         return HttpResponse('''<script>alert("current password is not matching");window.location="/changepassword"</script>''')



def complaint_sendreply(request,id):
    request.session['cid']=id
    return render(request,"admin/complaint_sendreply.html")


def senreply(request):
    rpy=request.POST['textfield']
    ob=complaint_table.objects.get(id= request.session['cid'])
    ob.reply=rpy
    ob.save()
    return HttpResponse('''<script>alert("sended");window.location="/viewcomplaints"</script>''')


def ForgotPassword(request):
    return render(request,"admin/ForgotPassword.html")


def ForgotPassword_post(request):
    text=request.POST['textfield']
    return HttpResponse('''<script>alert("Check your mail");window.location="/"</script>''')





def ManageDepartment(request):
    ob=department_table.objects.all()
    return render(request,"admin/ManageDepartment.html",{"val":ob})

def ManageDepartment_search(request):
    name=request.POST["textfield"]
    ob=department_table.objects.filter(department__contains=name)
    return render(request,"admin/ManageDepartment.html",{"val":ob})

def verifyhospital(request):
    ob=hospital_table.objects.filter(LOGIN__type='pending')
    return render(request,"admin/verifyhospital.html",{"val":ob})



def verifyhospitalsearch(request):
    name=request.POST['textfield']
    ob=hospital_table.objects.filter(LOGIN__type='pending',name__istartswith=name)
    return render(request,"admin/verifyhospital.html",{"val":ob})



def accept_hosp(request,id):
    ob=login_table.objects.get(id=id)
    ob.type="hospital"
    ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location="/verifyhospital"</script>''')


def reject_hosp(request,id):
    ob=login_table.objects.get(id=id)
    ob.type="rejected"
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location="/verifyhospital"</script>''')
def admin_view_accepted_hospital(request):
    ob=hospital_table.objects.filter(LOGIN__type='hospital')
    return render(request,"admin/admin_view_verified_hospital.html",{"val":ob})


def admin_view_accepted_hospital_search(request):
    name = request.POST["textfield"]
    ob=hospital_table.objects.filter(LOGIN__type='hospital',name__istartswith=name)
    return render(request,"admin/admin_view_verified_hospital.html",{"val":ob})

def admin_view_accepted_hospital(request):
    ob=hospital_table.objects.all()
    return render(request,"admin/admin_view_verified_hospital.html",{"val":ob})




def viewcomplaints(request):
    ob=complaint_table.objects.all()
    return render(request,"admin/viewcomplaints.html",{"vc":ob})

def viewcomplaints_search(request):
    date=request.POST["textfield"]
    ob=complaint_table.objects.filter(date__exact=date)
    return render(request,"admin/viewcomplaints.html",{"vc":ob})
# def viewcomplaints(request):


def viewdoctor(request,hosid):

    doc=doctor_table.objects.filter(HOSPITAL__id=hosid)
    return render(request,"admin/viewdoctor.html",{"doc":doc})

def admin_search_doctor(request):
    hosid=request.POST["hos"]
    doctor_details = doctor_table.objects.filter(HOSPITAL=hosid)
    return render(request,"admin/viewdoctor.html",{"doctor_details":doctor_details})

def viewpatient(request):
    ob = user_table.objects.all()
    return render(request,"admin/viewpatient.html",{"pd": ob})
def viewpatient_serach(request):
    name=request.POST["textfield"]
    ob = user_table.objects.filter(name__contains=name)
    return render(request,"admin/viewpatient.html",{"pd": ob})







# "+============================hospital====================================="

def HOS_Change_password(request):
    return render(request,"hospital/Change_password.html")

def changepassword_postHOS(request):
     cpassword=request.POST['p1']
     newpassword=request.POST['p2']
     conpassword=request.POST['p3']
     ob=login_table.objects.get(id=request.session['lid'])
     if ob.password == cpassword:
         if  newpassword==conpassword:
             ob.password=conpassword
             ob.save()
             return HttpResponse('''<script>alert("password changed");window.location="/changepassword"</script>''')
         else:
             return HttpResponse('''<script>alert("new password is not equal to conform password");window.location="/changepassword"</script>''')
     else:
         return HttpResponse('''<script>alert("current password is not matching");window.location="/changepassword"</script>''')



def hospitalhome(request):
    return render(request,"hospital/hospitalindex.html")
def Hospitalregister(request):
    return render(request,"hospital/reg.html")
    return render(request,"hospital/Hospitalregister.html")

def hospitalregistration_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield10']
    Post = request.POST['textfield11']
    Phone = request.POST['textfield3']
    Email = request.POST['textfield4']
    Latitude = request.POST['textfield5']
    Longitude = request.POST['textfield6']
    Username = request.POST['textfield7']
    Password = request.POST['textfield8']

    ob=login_table()
    ob.username=Username
    ob.password=Password
    ob.type='pending'
    ob.save()

    ob1=hospital_table()
    ob1.LOGIN=ob
    ob1.name=name
    ob1.place=place
    ob1.post=Post
    ob1.phone=Phone
    ob1.email=Email
    ob1.latitude=Latitude
    ob1.longitude=Longitude
    ob1.save()
    return HttpResponse('''<script>alert("Success");window.location="/"</script>''')


def ManageDoctor(request):
    ob=doctor_table.objects.filter(HOSPITAL__LOGIN__id=request.session["lid"])
    for i in ob:
        r=rating_table.objects.filter(DOCTOR__id=i.id)
        ar="Null"
        tr=0
        if len(r)>0:
            for j in r:
                tr+=j.rating
            ar=tr/len(r)
        i.r=ar
    return render(request,"hospital/ManageDoctor.html",{"data":ob})

def ManageDoctor_search(request):
    name=request.POST['textfield']
    ob=doctor_table.objects.filter(HOSPITAL__LOGIN__id=request.session["lid"],name__istartswith=name)
    for i in ob:
        r=rating_table.objects.filter(DOCTOR__id=i.id)
        ar="Null"
        tr=0
        if len(r)>0:
            for j in r:
                tr+=j.rating
            ar=tr/len(r)
        i.r=ar
    return render(request,"hospital/ManageDoctor.html",{"data":ob})
def hospital_delete_doctor(request,lid):
    ob=login_table.objects.get(id=lid).delete()
    return HttpResponse('''<script>alert("deleted");window.location="/ManageDoctor"</script>''')
def hospital_edit_doctor(request,id):
    ob=doctor_table.objects.get(id=id)
    ob2 = department_table.objects.all()
    return render(request,"hospital/Hospital_edit_doctor.html",{"data":ob,"dept":ob2})


def ManageDoctor_AddNew(request):
    ob=department_table.objects.all()

    return render(request,"hospital/ManageDoctor_AddNew.html",{"dept":ob})
def ManageDoctor_AddNew_post(request):
    name = request.POST['textfield2']
    age = request.POST['textfield']
    gender = request.POST['gen']
    qualifiction = request.POST['textfield3']
    specialization = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    DEPARTMENT = request.POST['ss']
    photo = request.FILES['file']
    username = request.POST['textfield7']
    password = request.POST['textfield8']



    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type='doctor'
    ob.save()

    ob1=doctor_table()
    ob1.LOGIN=ob
    ob1.name=name
    ob1.age=age
    ob1.gender=gender
    ob1.qualifiction=qualifiction
    ob1.specialization=specialization
    ob1.phone=phone
    ob1.email=email
    ob1.DEPARTMENT_id=DEPARTMENT
    ob1.HOSPITAL=hospital_table.objects.get(LOGIN__id=request.session["lid"])
    ob1.photo=photo
    ob1.save()
    return HttpResponse('''<script>alert("Success");window.location="/ManageDoctor"</script>''')


def ManageSchedule(request,id):
    request.session['did']=id
    ob=schedule_table.objects.filter(DOCTOR__id=id)
    return render(request,"hospital/ManageSchedule.html",{"val":ob})

def ManageSchedule_AddNew(request):

    return render(request,"hospital/sch_form.html")
from datetime import datetime, timedelta


def find_day(date_string):
    # Convert the date string to a datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    # Get the day of the week (e.g., Monday, Tuesday)
    return date_object.strftime('%A')

def list_days_between(start_date_string, end_date_string):
    # Convert the date strings to datetime objects
    start_date = datetime.strptime(start_date_string, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_string, '%Y-%m-%d')

    # Initialize a list to hold all the dates
    date_list = []

    # Iterate through the range of dates
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return date_list

def ManageSchedule_AddNew_POST(request):
    Ftime = request.POST['ft']
    Ttime = request.POST['tt']
    fdate = request.POST['fd']
    tdate = request.POST['td']
    days=request.POST.getlist("d")
    daylist = list_days_between(fdate,tdate)
    for i in daylist:
        if find_day(i) in days:
            ob=schedule_table()
            ob.DOCTOR_id=request.session['did']
            ob.fromtime=Ftime
            ob.totime=Ttime
            ob.date=i
            ob.save()

    return ManageSchedule(request,request.session["did"])

def hos_delete_schedules(request,schid):
    ob=schedule_table.objects.get(id=schid).delete()
    return ManageSchedule(request, request.session["did"])







def ViewBooking(request):
    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__HOSPITAL__LOGIN=request.session["lid"])
    print(ob)
    return render(request,"hospital/ViewBooking.html",{"data":ob})

def ViewBooking_search(request):
    date=request.POST["date"]
    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__HOSPITAL__LOGIN=request.session["lid"],date__exact=date)
    print(ob)
    return render(request,"hospital/ViewBooking.html",{"data":ob})


def ViewBooking_Schedule(request):
    return render(request,"hospital/ViewBooking_Schedule.html")
def ViewProfile(request):
    ob=hospital_table.objects.get(LOGIN=request.session["lid"])

    return render(request,"hospital/ViewProfile.html",{"data":ob})

def update_hosp_profile(request):
    name=request.POST['name']
    post=request.POST['post']
    place = request.POST['place']
    phone = request.POST['phone']
    email = request.POST['email']
    ob=hospital_table.objects.get(LOGIN__id=request.session["lid"])
    ob.name=name
    ob.place=place
    ob.post=post
    ob.phone=phone
    ob.email=email
    ob.save()
    return render(request,"hospital/ViewProfile.html",{"data":ob})

# "+===========================doctor==============================="
def DoctorHome(request):
    return render(request, "doctor/doctorindex.html")
def ManageBooking(request):
    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN__id=request.session['lid'])
    return render(request,"doctor/ManageBooking.html",{'val':ob})


def searchManageBooking(request):
    name=request.POST['textfield']
    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN__id=request.session['lid'],date=name)
    return render(request,"doctor/ManageBooking.html",{'val':ob})



def accept_booking(request,id):
    ob=booking_table.objects.get(id=id)
    ob.status="accept"
    ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location="/ManageBooking"</script>''')


def reject_booking(request,id):
    ob=booking_table.objects.get(id=id)
    ob.status="rejected"
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location="/ManageBooking"</script>''')






def ViewBooking1(request):

    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN__id=request.session['lid'])
    print(ob,"gggggggggg")
    return render(request,"doctor/ViewBooking1.html",{'val':ob})

def acceptbooking(request,id):
    ob=booking_table.objects.get(id=id)
    ob.status="accepted"
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location="/ViewBooking1"</script>''')


def rejectbooking(request,id):
    ob=booking_table.objects.get(id=id)
    ob.status="rejected"
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location="/ViewBooking1"</script>''')



def ViewBooking1search(request):
    date=request.POST['textfield']
    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN__id=request.session['lid'],date=date)
    return render(request,"doctor/ViewBooking1.html",{'val':ob})

def ViewBooking1_Prescription(request,id):
    request.session['bookid']=id
    kk=prescription_table.objects.filter(BOOK__id= request.session['bookid'])
    return render(request,"doctor/ViewBooking1_Prescription.html",{'val':kk})


def ViewBooking1_Prescription_AddNew(request):
    return render(request,"doctor/ViewBooking1_Prescription_Add New.html")



def ViewBooking1_Prescription_AddNew_post(request):
    pre=request.POST['textfield']
    rep=request.POST['textfield2']
    img=request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(img.name, img)
    obb=booking_table.objects.get(id=request.session['bookid'])
    obb.status='Added'
    obb.save()
    ob=prescription_table()
    ob.prescription=pre
    ob.files=fsave
    ob.report=rep
    ob.datee=datetime.now().date()
    ob.BOOK=booking_table.objects.get(id=request.session['bookid'])
    ob.save()
    return HttpResponse('''<script>alert("added");window.location="/ViewBooking1"</script>''')


def deleteprescription(request,id):
    ob=prescription_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/ViewBooking1"</script>''')




def ViewBookingHistory(request):
    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN__id=request.session['lid'])
    return render(request,"doctor/ViewBookingHistory.html",{"val":ob})

def searchViewBookingHistory(request):
    date=request.POST['textfield']
    ob=booking_table.objects.filter(date=date,SCHEDULE__DOCTOR__LOGIN__id=request.session['lid'])
    return render(request,"doctor/ViewBookingHistory.html",{"val":ob})

def viewrating(request):
    ob=rating_table.objects.filter(DOCTOR__LOGIN__id=request.session['lid'])
    return render(request,"doctor/viewrating.html",{'val':ob})




def viewratingsearch(request):
    data=request.POST['textfield']
    ob=rating_table.objects.filter(DOCTOR__LOGIN__id=request.session['lid'],date=data)
    return render(request,"doctor/viewrating.html",{'val':ob})





def ViewSchedule(request):
    ob=schedule_table.objects.filter(DOCTOR__LOGIN__id=request.session['lid'])
    return render(request,"doctor/ViewSchedule.html",{'data':ob})






def viewdocprofile(request):
    ob=doctor_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"doctor/viewprofile.html",{'data':ob})

def viewdocprofilecode(request):
    ob=doctor_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"doctor/doctorupdateprofile.html",{'data':ob})






def viewdocprofileupdate(request):
    ob=doctor_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"doctor/UPDATE PFOFILE.html",{'data':ob})

def updatedoctorprofile(request):
    if "file" in request.FILES:
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        qualifiction = request.POST['qualifiction']
        specialization = request.POST['specialization']
        phone = request.POST['phone']
        email = request.POST['email']
        # DEPARTMENT = request.POST['photo']
        photo = request.FILES['file']
        fs=FileSystemStorage()
        fsave=fs.save(photo.name,photo)
        ob1=doctor_table.objects.get(LOGIN__id=request.session['lid'])
        ob1.name=name
        ob1.age=age
        ob1.gender=gender
        ob1.qualifiction=qualifiction
        ob1.specialization=specialization
        ob1.phone=phone
        ob1.email=email
        # ob1.DEPARTMENT_id=DEPARTMENT
        # ob1.HOSPITAL=hospital_table.objects.get(LOGIN__id=request.session["lid"])
        ob1.photo=fsave
        ob1.save()
        return HttpResponse('''<script>alert("Success");window.location="/viewdocprofile"</script>''')
    else:
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        qualifiction = request.POST['qualifiction']
        specialization = request.POST['specialization']
        phone = request.POST['phone']
        email = request.POST['email']
        ob1 = doctor_table.objects.get(LOGIN__id=request.session['lid'])
        ob1.name = name
        ob1.age = age
        ob1.gender = gender
        ob1.qualifiction = qualifiction
        ob1.specialization = specialization
        ob1.phone = phone
        ob1.email = email
        # ob1.DEPARTMENT_id = DEPARTMENT
        # ob1.HOSPITAL = hospital_table.objects.get(LOGIN__id=request.session["lid"])
        ob1.save()
        return HttpResponse('''<script>alert("Success");window.location="/ManageDoctor"</script>''')


def changepasswordDOC(request):
    return render(request,"doctor/CHANGE PASSWORD DOC.html")

def changepassword_postDOC(request):
     cpassword=request.POST['currentpassword']
     newpassword=request.POST['Newpassword']
     conpassword=request.POST['Confirmpassword']
     ob=login_table.objects.get(id=request.session['lid'])
     if ob.password == cpassword:
         if  newpassword==conpassword:
             ob.password=conpassword
             ob.save()
             return HttpResponse('''<script>alert("password changed");window.location="/changepassword"</script>''')
         else:
             return HttpResponse('''<script>alert("new password is not equal to conform password");window.location="/changepassword"</script>''')
     else:
         return HttpResponse('''<script>alert("current password is not matching");window.location="/changepassword"</script>''')




def user_reg(request):
    return render(request,'user/reg.html')
    return render(request,'user/userform_reg.html')


def userregistration(request):
    Name = request.POST['textfield']
    Gender = request.POST['radiobutton']
    Age = request.POST['textfield2']
    Place = request.POST['textfield3']
    Post = request.POST['textfield4']
    Phone = request.POST['textfield5']
    Email = request.POST['textfield6']
    Photo = request.POST['file']
    username = request.POST['textfield7']
    password = request.POST['textfield8']

    ob = login_table()
    ob.username=username
    ob.password=password
    ob.type="user"
    ob.save()

    obb=user_table()
    obb.LOGIN=ob
    obb.name=Name
    obb.gender=Gender
    obb.age=Age
    obb.place=Place
    obb.post=Post
    obb.phone=Phone
    obb.email=Email
    obb.photo=Photo





    obb.save()
    return HttpResponse('''<script>alert('success');window.location='/'</script>''')


def userhome(request):
    return render(request,"user/userindex.html")
def user_view_hospital(request):
    ob=hospital_table.objects.all()
    return render(request,'user/verifyhospital.html',{"val":ob})
def user_view_hospital_serach(request):
    name=request.POST["textfield"]
    ob=hospital_table.objects.filter(name__contains=name)
    return render(request,'user/verifyhospital.html',{"val":ob})


def user_view_doctor(request,hid):
    ob=doctor_table.objects.filter(HOSPITAL=hid)
    return render(request,"user/doctor.html",{"doc":ob})


def viewprofileuser(request):
    ob=user_table.objects.get(LOGIN=request.session["lid"])
    return render(request,"user/user view profile.html",{"doc":ob})




def user_view_doctor_review(request,rid):
    ob=rating_table.objects.filter(DOCTOR=rid)
    return render(request,'user/Review.html',{"data":ob})

def User_Scheduleform(request,did):
    ob=schedule_table.objects.filter(DOCTOR=did,date__gt=datetime.now().date())
    return render(request,"user/Scheduleform.html",{"data":ob})
def user_book_doctor(request,schid):
    ob=booking_table()
    ob.USER=user_table.objects.get(LOGIN=request.session["lid"])
    ob.SCHEDULE_id=schid
    ob.date=datetime.now().date()
    ob.status="pending"
    ob.save()

    return HttpResponse('''<script>alert('success');window.location='/user_view_hospital'</script>''')

def Bookappointment(request):
    ob = booking_table.objects.filter(USER__LOGIN=request.session["lid"]).order_by('-id')
    print (ob,"ggggg")
    return render(request, "user/Bookappointment.html", {"doc": ob})


def Complaints(request):
    ob = complaint_table.objects.filter(USER__LOGIN=request.session["lid"]).order_by('-id')
    return render(request,"user/Complaints.html",{"data":ob})


def Complaints_delete(request,cid):
    ob = complaint_table.objects.get(id=cid).delete()
    return HttpResponse('''<script>alert('success');window.location='/Complaints#a'</script>''')


def Send_Complaint(request):
    return render(request,"user/Send_Complaint.html")
def Send_Complaint_post(request):
    comp=request.POST["textfield"]
    ob=complaint_table()
    ob.USER=user_table.objects.get(LOGIN=request.session["lid"])
    ob.complaint=comp
    ob.date=datetime.now().date()
    ob.reply="pending"
    ob.save()

    return HttpResponse('''<script>alert('success');window.location='/Complaints#a'</script>''')


def Review(request):
    return render(request,"user/Review.html")

def userform(request):
    return render(request,"user/userform.html")

def view_prescription_user(request,id):
    ob=prescription_table.objects.filter(id=id)
    return render(request,"user/viewprescription.html",{"val":ob})

# def user_updateprofile_post(request):
#     id = request.POST['id']
#     Name = request.POST['name']
#     Gender = request.POST['gender']
#     Age = request.POST['age']
#     Place = request.POST['place']
#     Post = request.POST['post']
#     Phone = request.POST['phone']
#     Email = request.POST['email']
#
#
#     obb=user_table.objects.get(id=id)
#     obb.LOGIN=login_table.objects.get(id=request.session['lid'])
#     if 'file' in request.POST:
#         Photo = request.POST['file']
#         obb.photo = Photo
#
#     obb.name=Name
#     obb.gender=Gender
#     obb.age=Age
#     obb.place=Place
#     obb.post=Post
#     obb.phone=Phone
#     obb.email=Email
#
#
#
#
#
#     obb.save()
#     return HttpResponse('''<script>alert('success');window.location='/viewprofileuser'</script>''')



from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def user_updateprofile_post(request):
    id = request.POST['id']
    Name = request.POST['name']
    Gender = request.POST['gender']
    Age = request.POST['age']
    Place = request.POST['place']
    Post = request.POST['post']
    Phone = request.POST['phone']
    Email = request.POST['email']
    uploaded_file = request.FILES['file']

    obb = user_table.objects.get(id=id)
    obb.LOGIN = login_table.objects.get(id=request.session['lid'])

    # if 'file' in request.FILES:
    #     uploaded_file = request.FILES['file']
    #     fs = FileSystemStorage()
    #     filename = fs.save(uploaded_file.name, uploaded_file)
    #     obb.photo = fs.url(filename)

    obb.photo = uploaded_file
    obb.name = Name
    obb.gender = Gender
    obb.age = Age
    obb.place = Place
    obb.post = Post
    obb.phone = Phone
    obb.email = Email

    # Save the updated object to the database
    obb.save()

    return HttpResponse('''<script>alert('Profile updated successfully!');window.location='/viewprofileuser'</script>''')





















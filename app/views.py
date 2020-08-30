from django.shortcuts import render,redirect
import random
from captcha.image import ImageCaptcha
from app.models import Admin,SavingAccount,Statement
from django.db.models import Max
from django.core.mail import send_mail

from YesBank.settings import EMAIL_HOST_USER

ran = 0
def showIndex(request):
    return render(request,"index.html")

def generate_captcha():
    global ran
    ran = random.randint(100000, 999999)
    ic = ImageCaptcha()
    ic.write(str(ran), "app/static/cimg/captcha.png")

def createAccount():
    res = SavingAccount.objects.all().aggregate(Max('acno'))
    if res['acno__max']:
        acno = res['acno__max']+1
        return acno
    else:
        return 72450001

def password_generator():
    pas = random.randint(1000,9999)
    return pas

def ref_generator():
    rno = random.randint(100000,999999)
    return rno

def admin_login(request):
    generate_captcha()
    return render(request,"admin_login.html")

def user_login(request):
    generate_captcha()
    return render(request,"user_login.html")

def about_us(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")

def bank_with_us(request):
    return render(request,"bank_with_us.html")

def work_with_us(request):
    return render(request,"work_with_us.html")

def admin_check(request):
    un = request.POST.get("t1")
    pas = request.POST.get("t2")
    code = int(request.POST.get("t3"))
    if ran == code:
        try:
            res = Admin.objects.get(uname=un,password=pas)
            return render(request,"admin_home.html")
        except Admin.DoesNotExist:
            return render(request,"admin_login.html",{"error":"Invalid user"})
    else:
        return render(request,"admin_login.html",{"error":"Invalid Security Code"})

def admin_home(request):
    return render(request,"admin_home.html")

count = 0
def user_check(request):
    un = request.POST.get("t1")
    pas = request.POST.get("t2")
    global count
    code = int(request.POST.get("t3"))
    if ran == code:
        try:
            ures = SavingAccount.objects.get(acno=un,password=pas)
            if ures.status == "Active":
                count = 0
                request.session['acno'] = ures.acno
                return render(request, "user_home.html",{"udata":ures})
            elif ures.status == "Blocked":
                count = 0
                return render(request, "user_login.html", {"blocked": "Sorry Your Account is Blocked"})
            else:
                count = 0
                return render(request, "user_login.html", {"closed": "Sorry Your Account is Closed"})
        except SavingAccount.DoesNotExist:
            count+=1
            if count == 3:
                status = "Blocked"
                SavingAccount.objects.filter(acno=un).update(status=status)
                count = 0
                return render(request, "user_login.html",{"msg":"Sorry Your Account is Blocked"})
            else:
                return render(request, "user_login.html", {"error": "Invalid Password","data":count+1})
    else:
        return render(request, "user_login.html", {"error1": "Invalid Security Code"})


def admin_refresh(request):
    generate_captcha()
    return render(request,"admin_login.html")

def user_refresh(request):
    generate_captcha()
    return render(request,"user_login.html")

def create_account(request):
    #res = SavingAccount.objects.all().aggregate(Max('acno'))
    #print(res)
    #print(acno)
    return render(request,"create_account.html")

def save_account(request):
    acno = createAccount()
    pas = password_generator()
    fn = request.POST.get("t1")
    ln = request.POST.get("t2")
    ftn = request.POST.get("t3")
    mn = request.POST.get("t4")
    dob = request.POST.get("t5")
    gen = request.POST.get("t6")
    ano = request.POST.get("t7")
    nat = request.POST.get("t8")
    mno = request.POST.get("t9")
    em = request.POST.get("t10")
    img = request.FILES['t11']
    sig = request.FILES['t12']
    hn = request.POST.get("t13")
    sn = request.POST.get("t14")
    vill = request.POST.get("t15")
    ct = request.POST.get("t16")
    po = request.POST.get("t17")
    pin = request.POST.get("t18")
    stat = request.POST.get("t19")
    dist = request.POST.get("t20")
    SavingAccount(acno=acno,fname=fn,lname=ln,ftname=ftn,mname=mn,dob=dob,gender=gen,adhar=ano,national=nat,mobile=mno,email=em,
                  photo=img,sign=sig,password=pas,house=hn,street=sn,village=vill,city=ct,post=po,pin=pin,state=stat,dist=dist).save()
    return render(request,'create_account.html',{"msg":"Account is Created","data":acno})

def view_all_account(request):
    res = SavingAccount.objects.all()
    return render(request,"view_all_account.html",{"data":res})

def activate_account(request):
    return render(request,"activate_account.html")

def active_acc(request):
    ac = request.POST.get("t1")
    status = "Active"
    try:
        SavingAccount.objects.get(acno=ac)
        SavingAccount.objects.filter(acno=ac).update(status=status)
        return render(request,"activate_account.html",{"msg":"Account Activated !!!"})
    except SavingAccount.DoesNotExist:
        return render(request,"activate_account.html",{"error":"Invalid Account Number !!!"})

def change_password(request):
    return render(request,"change_password.html")

def update_password(request):
    oldpas = request.POST.get("t1")
    newpas = request.POST.get("t2")
    try:
        Admin.objects.get(password=oldpas)
        Admin.objects.filter(password=oldpas).update(password=newpas)
        return render(request,"change_password.html",{"msg":"Password changed Successfully"})
    except Admin.DoesNotExist:
        return render(request,"change_password.html",{"error":"Invalid Old Password"})

def close_account(request):
    return render(request,"close_account.html")

def clos_acc(request):
    ac = request.POST.get("t1")
    status = "Closed"
    try:
        SavingAccount.objects.get(acno=ac)
        SavingAccount.objects.filter(acno=ac).update(status=status)
        return render(request,"close_account.html",{"msg":"Account is Closed"})
    except SavingAccount.DoesNotExist:
        return render(request,"close_account.html",{"error":"Invalid Account number"})

def user_home(request):
    #ac = request.GET.get("no")
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"user_home.html",{"udata":ures})

def deposit_form(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"deposit_form.html",{"udata":ures})

def withdraw_form(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"withdraw_form.html",{"udata":ures})

def deposit_amt(request):
    damt = float(request.POST.get("t2"))
    res = SavingAccount.objects.get(acno=request.session['acno'])
    balance = res.balance+damt
    SavingAccount.objects.filter(acno=request.session['acno']).update(balance=balance)
    refno = ref_generator()
    part = "Cash Deposit Cr"
    Statement(acno=request.session['acno'],reference=refno,particular=part,credit=damt,balance=balance).save()
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"user_home.html",{"udata":ures,"msg":"Amount is Deposited"})

def withdraw_amt(request):
    wamt = float(request.POST.get("t2"))
    res = SavingAccount.objects.get(acno=request.session['acno'])
    if res.balance > wamt:
        balance = res.balance - wamt
        SavingAccount.objects.filter(acno=request.session['acno']).update(balance=balance)
        refno = ref_generator()
        part = "Cash Withdraw Dr"
        Statement(acno=request.session['acno'], reference=refno, particular=part, debit=wamt, balance=balance).save()
        ures = SavingAccount.objects.get(acno=request.session['acno'])
        return render(request,"user_home.html",{"udata":ures,"msg":"Amount is Withdraw"})
    else:
        ures = SavingAccount.objects.get(acno=request.session['acno'])
        return render(request, "user_home.html", {"udata": ures, "msg": "Insufficient Balance"})

def balance_check(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"user_home.html",{"udata":ures,"message":"Your Current Balance is : "})

def transfer_form(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"transfer_form.html",{"udata":ures})

def transfer_amt(request):
    accno = request.POST.get("t2")
    tamt = float(request.POST.get("t3"))
    try:
        tres = SavingAccount.objects.get(acno=accno)
        res = SavingAccount.objects.get(acno=request.session['acno'])
        if res.balance > tamt:
            balance = res.balance - tamt
            SavingAccount.objects.filter(acno=request.session['acno']).update(balance=balance)
            refno = ref_generator()
            part = "Cash Transfer Dr"
            Statement(acno=request.session['acno'], reference=refno, particular=part,debit=tamt ,balance=balance).save()

            tbalance = tres.balance + tamt
            SavingAccount.objects.filter(acno=accno).update(balance=tbalance)
            refno = ref_generator()
            part = "Cash Transfer Cr"
            Statement(acno=accno, reference=refno, particular=part, credit=tamt,balance=balance).save()
            ures = SavingAccount.objects.get(acno=request.session['acno'])
            return render(request, "user_home.html", {"udata": ures, "msg": "Amount is Transfered "})
        else:
            ures = SavingAccount.objects.get(acno=request.session['acno'])
            return render(request, "transfer_form.html", {"udata": ures, "msg": "Insufficient Balance !!"})
    except SavingAccount.DoesNotExist:
        ures = SavingAccount.objects.get(acno=request.session['acno'])
        return render(request,"transfer_form.html",{"udata":ures,"msg":"Invalid Account Number !!"})

def change_pin_form(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"change_pin_form.html",{"udata":ures})

def change_pin(request):
    pin = request.POST.get("t2")
    npin = request.POST.get("t3")
    try:
        SavingAccount.objects.get(acno=request.session['acno'],password=pin)
        SavingAccount.objects.filter(acno=request.session['acno']).update(password=npin)
        ures = SavingAccount.objects.get(acno=request.session['acno'])
        return render(request, "user_home.html", {"udata": ures,"msg":"Password Changed Successfully"})
    except SavingAccount.DoesNotExist:
        ures = SavingAccount.objects.get(acno=request.session['acno'])
        return render(request,"change_pin_form.html",{"udata":ures,"msg":"Invalid Old Password"})

def current_account(request):
    return render(request,"current_account.html")

def fd_account(request):
    return render(request,"FD_account.html")

def fast_cash(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"fast_cash.html",{"udata":ures})

def services(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    return render(request,"services.html",{"udata":ures})

def forgot_pass_form(request):
    return render(request,"forgot_pass_form.html")

def mini_statement(request):
    ures = SavingAccount.objects.get(acno=request.session['acno'])
    udata = Statement.objects.filter(acno=request.session['acno'])
    return render(request,"mini_statement.html",{"data":udata,"udata":ures})

def forgot_password(request):
    acno = request.POST.get("t2")
    mob = request.POST.get("t3")
    email = request.POST.get("t4")
    try:
        res = SavingAccount.objects.get(acno=acno,mobile=mob,email=email)
        send_to = request.POST.get("t4").split(",")
        send_to_subject = "Forgot Password"
        send_to_message = "Your Password is : "+str(res.password)
        send_mail(send_to_subject, send_to_message, EMAIL_HOST_USER, send_to)
        return render(request,"forgot_pass_form.html",{"msg":"Password Send Your Registered Email-Id"})
    except SavingAccount.DoesNotExist:
        return render(request,"forgot_pass_form.html",{"error":"Invalid Details"})
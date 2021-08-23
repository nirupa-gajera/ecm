from django.shortcuts import render,redirect
from .models import *
from uuid import uuid4
from django.http import HttpResponse, request
from django.core.mail import send_mail
import math, random
import smtplib
import os
import json
from django.http import JsonResponse
from django.contrib import messages

# import messages


# Create your views here.
def Register(request):
    if request.method=="POST":
        fullname=request.POST["fullname"]
        email=request.POST["email"]
        dob=request.POST["dob"]		
        mobile=request.POST["mobile"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        city=request.POST["city"]
        password=request.POST["password"]
        upload1=request.FILES["upload"]
        
        request.session['pnm']=fullname       
         
        valid=register()
        valid.fullname=fullname
        valid.email=email
        valid.mobile=mobile
        valid.dob=dob
        valid.gender=gender
        valid.address=address
        valid.city=city
        valid.password=password
        valid.upload=upload1
        valid.save()
        return redirect("login")
    return render(request,"rpage.html")
def login(request):
    if request.POST:
        email1=request.POST["email"]
        Password1=request.POST["password"]
        n1=register.objects.get(email=email1)
        try:
            if n1:
                if n1.password == Password1:
                    request.session["nm"]=n1.email
                    
                    return redirect('pro')
                else:
                    messages.add_message(request, messages.ERROR, "Your password does not match!!")
            else:
                messages.add_message(request, messages.ERROR, "Your email id does not match!!")
        except:
            messages.add_message(request, messages.ERROR, "Your email id does not match!!")

            
    return render(request,"login.html")

                
    
    
def show(request):

	data = register.objects.all()


	return render(request,"show.html",{'hello':data})


def edit(request,id):  
	Check=register.objects.get(id=id)
	if request.POST:
		Check.fullname=request.POST['fullname']
		Check.email=request.POST['email']
		Check.mobile=request.POST['mobile']
		Check.dob=request.POST['dob']
		Check.gender=request.POST['gender']
		Check.address=request.POST['address']
		Check.city=request.POST['city']
		Check.password=request.POST['password']
		Check.upload1=request.FILES['upload']


		Check.save()
	return render(request,"edit.html",{'editdata':Check})

# def delete(request,id):  
#     regis.delete()  
#     return redirect("/show")

def download(request,id):
	regi = register.objects.get(id=id)
	regi.download()
	return redirect("/show")

def email(request):
    if request.method == "POST":
        gmail = request.POST.get("from")
        password = request.POST.get("password")
        to = request.POST.get("to")
        message = request.POST.get("message")
        print(gmail)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(gmail,password)
        print(message)
        s.sendmail(gmail,to,message)
        s.quit()
        print("Mail Sent")
    return render(request, "mail.html")

def send_otp(request):
    # if request.POST:
    # 	gmail = request.POST.get("from")
    # 	password = request.POST.get("password")
    # 	to = request.POST.get("to")
    # 	otp = request.POST.get("otp")
    # 	request.session['email1']=to
    # 	print("mail",gmail)
    # 	valid=register.objects.get(email=to)
    # 	otp = random.randint(1000, 9999)
    # 	otp = str(otp)
    # 	print("otp number",otp)
    #     s=smtplib.SMTP('smtp.gmail.com',587)
    #     s.starttls()
    #     s.login("noreply.jenu@gmail.com","patel67&")
    #     s.sendmail("noreply.jenu@gmail.com",to,otp)
    #     s.quit()
    #     request.session['otp']=otp
    #     return render(request,'ocheck.html')
       
            # messages.add_message(request, messages.ERROR, "You Have Entered Wrong email ")
            # return render(request,"otp.html")
    return render(request,"otp.html")
    



def otpcheck(request):
    # if request.session.has_key('otp'):
    #     if request.POST:
    #         otp = request.POST['otp']
    #         if int(request.session['otp']) == int(otp):
    #             del request.session['otp']
               
    #             return redirect('password')
    #         else:
    #             messages.add_message(request, messages.ERROR, "You Have Entered Wrong OTP ")
    #             #return HttpResponse("<h2><a href=""> You Have Entered Wrong OTP </a></h2>")
    #     else:
    #         return redirect('password')
    return render(request,"ocheck.html")


def Password(request):
    # gmail = request.POST.get("to")
    # password = request.POST.get("password")
    # print("session",request.session.get('email1'))
    # data=register.objects.get(email=request.session.get('email1'))
    # if request.POST:
    #     passw=request.POST['newpassword']
    #     passw1=request.POST['confirmpassword']
    #     # data.password=request.POST['password']
        

    #     if passw==passw1:
    #         data.password=passw1
    #         data.save()
            
    #         messages.add_message(request,messages.ERROR,"Password succesfully change...")

    #     else:
    #         messages.add_message(request,messages.ERROR,"Did not match to newpassword...")
    # else:
    return render(request,'password.html')
    # return render(request,"password.html",{"data":data})

def rename(request):
    data = register.objects.all()

    return render(request,"rename.html",{'hello':data})

def Rename(request,id):  
	Check=register.objects.get(id=id)
	if request.POST:
		
		if request.FILES.get('upload')==None:
			print("pass")
			pass
		else:
			print("else")
			Check.upload=request.FILES['upload']
		Check.fullname=request.POST['txt']
	

		Check.save()
	return render(request,"rename.html",{'editdata':Check})



def Product(request):
    if 'nm' in request.session.keys():
        print(request.session.get("nm"))
        user=register.objects.get(email=request.session.get('nm'))
        

        if request.POST:
            pname1=request.POST["pname"]
            pquantity1=request.POST["pquantity"]
            pprice=request.POST["pprice"]
            pdesc=request.POST["pdesc"]
            pimage=request.FILES["pimage"]
            print("session",request.session.get('pnm'))
            valid = product(
                
                name=user,
                pname=pname1,
                pquantity=pquantity1,
                pprice=pprice,
                pdesc=pdesc,
                pimage=pimage,
            )
            
            valid.save()
        return render(request,"product.html",{'user1':user})
    else:
        print("not valid")
    return render(request,"product.html")


# def Person(request):
#     if request.POST:
#             age1=request.POST["age"]
#             mail1=request.POST["email"]
#             print("session",request.session.get('pnm'))
#             am=product.objects.get(pname=request.session.get('pnm'))
#             valid = person(
#                 name=am,
#                 age=am.pprice,
#                 email=mail1,
#             )
            

#             valid.save()
#         return render(request,"dat.html")
#     else:
#         print("not valid..")

def logout(request):
    if "nm" in request.session:
        del request.session["nm"] 
        print("none")
        return redirect("reg")
    else:
        pass
        
        


def categories(request):
    if 'nm' in request.session.keys():
        print(request.session.get("nm"))
        # a1=register.objects.get(email=request.session.get('nm'))
        user=vendor.objects.get(email=request.session.get('nm'))

        
        h1=category.objects.all()
        h2=subcategory.objects.all()
        if request.POST:
            name1=request.POST["name"]
            brand1=request.POST["brand"]
            quantity1=request.POST["quantity"]
            price1=request.POST["price"]
            desc1=request.POST["desc"]
            image1=request.FILES["image"]
            a2=category.objects.get(name=request.POST['names'])
            a3=subcategory.objects.get(name=request.POST['cnames'])

            
            valid = productss(
                admin=user,
                cate=a2,
                subcate=a3,
                name=name1,
                price=price1,
                brand=brand1,
                quantity=quantity1,
                desc=desc1,
                image=image1,
            )
            
            valid.save()
            
            return render(request,"vendor/categories.html",{'cat':a2,'user2':a3})

        return render(request,"vendor/categories.html",{'user1':user,'data':h1,'data2':h2})
    else:
        return redirect("login")
    return render(request,"categories.html")

def cart1(request,id):
    if 'nm' in request.session.keys():
        # h2=productss.objects.all()
        h1=productss.objects.get(id=id)
        if request.POST:
            h1.name1=request.POST["name"]
            h1.brand1=request.POST["brand"]
            h1.quantity1=request.POST["quantity"]
            h1.price1=request.POST["price"]
            h1.desc1=request.POST["desc"]
            h1.image1=request.FILES["image"]
            
            h1.save()
            
        return render(request,"cart.html",{'data':h1})
    
def Admin(request):
    if request.method=="POST":
        fullname=request.POST["fullname"]
        email=request.POST["email"]
        dob=request.POST["dob"]		
        mobile=request.POST["mobile"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        city=request.POST["city"]
        password=request.POST["password"]
        upload1=request.FILES["upload"]
        
        request.session['pnm']=fullname       
         
        valid=vendor()
        valid.fullname=fullname
        valid.email=email
        valid.mobile=mobile
        valid.dob=dob
        valid.gender=gender
        valid.address=address
        valid.city=city
        valid.password=password
        valid.upload=upload1
        valid.save()
        return redirect("adlogin")
    return render(request,"vendor/admin1.html")

def adminlogin(request):
    if request.POST:
        email1=request.POST["email"]
        Password1=request.POST["password"]
        n1=vendor.objects.get(email=email1)
        try:
            if n1:
                if n1.password == Password1:
                    request.session["nm"]=n1.email
                    
                    return redirect("cat")

                else:
                    messages.add_message(request, messages.ERROR, "Your password does not match!!")
            else:
                messages.add_message(request, messages.ERROR, "Your email id does not match!!")
        except:
            messages.add_message(request, messages.ERROR, "Your email id does not match!!")
   
    return render(request,"vendor/adminlogin.html")

def adminlogout(request):
    if "nm" in request.session:
        del request.session["nm"] 
        print("none")
        return redirect("vendor")
    else:
        pass
def pro(request):
    if request.session.keys():
        h1=productss.objects.all()
        a1=register.objects.get(email=request.session.get('nm'))
        a2=subcategory.objects.all()
        
        myList=[]
        if 'sub1' in request.POST:
            p1=request.POST["price"]
            p2=request.POST["price1"]
            print(p1,p2)
            for i in h1:
                if i.price>int(p1) and i.price<int(p2):
                    myList.append(i)
            return render(request,"pro.html",{'user1':a1,'data2':a2,'myList':myList})

        if 'sub2' in request.POST:
            print("hello")
            c1=subcategory.objects.get(name=request.POST["subcategory"])   
            p1=productss.objects.filter(subcate=c1)
                
            return render(request,'subcat.html',{'cat1':c1,'prod1':p1})
       
        
        return render(request,"pro.html",{'data':h1,'user1':a1,'data2':a2})
    else:
        print("session not available")
        
def autocomplete(request):
    if 'term' in request.GET:
        qs = subcategory.objects.filter(name__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            print("data",product.name)
            titles.append(product.name)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'pro.html')

def Add_cart(request,id):
  
    if 'nm' in request.session.keys():
        print("session",request.session.get("nm"))
        print("calling..")
        a1=register.objects.get(email=request.session.get('nm'))
        a3=productss.objects.get(id=id)
        a2=vendor.objects.get(fullname=a3.admin)
    
        valid=cart()
        valid.user=a1
        valid.vendor=a2
        valid.name=a3
        valid.save()
        return redirect("Show_cart")   
        cartdata=cart.objects.filter(user=a1)
        return render(request,"cart.html",{'user1':a1,'h2':a2,'h3':a3,'cart':cartdata})
    # return render(request,"cart.html",{'user1':a1,'h2':a2,'h3':a3,'cart':cartdata})

def Show_cart(request):
    if 'nm' in request.session.keys():
        a1=register.objects.get(email=request.session.get('nm'))
        
        cartdata=cart.objects.filter(user=a1)
    return render(request,"cart.html",{'user1':a1,'cart':cartdata})


def delete(request,id):
    if 'nm' in request.session.keys():
        data=cart.objects.get(id=id)
        data.delete()
    return redirect('/Show_cart')

def Address(request):
    if 'nm' in request.session.keys():
        a1=register.objects.get(email=request.session.get('nm'))
        if request.POST:
            fullname=request.POST["fname"]
            mobile1=request.POST["mobile"]
            home=request.POST["home_no"]		
            landmark1=request.POST["landmark"]
            city1=request.POST["city"]
            pincode1=request.POST["pincode"]
            state1=request.POST["state"]
            type1=request.POST["type"]
            
            print("inside")
            valid=address()
            valid.fname=fullname
            valid.mobile=mobile1
            valid.home_no=home
            valid.landmark=landmark1
            valid.city=city1
            valid.pincode=pincode1
            valid.state=state1
            valid.type=type1
            valid.save()
            print("data Added")
            # return redirect("cart")
        else:
            messages.add_message(request, messages.ERROR, "Your data cannot save!")

        return render(request,"address.html",{'user1':a1})
    
# def editadd(request,id):
#     Check=register.objects.get(id=id)
#     if request.POST:
#         Check.fullname=request.POST['fullname']
#         Check.mobile=request.POST['mobile']
#         Check.address=request.POST['address']
#         Check.city=request.POST['city']
        
#         Check.save()
#     return render(request,"addedit.html",{'editdata':Check})

    

def Buy(request,id):
    if 'nm' in request.session.keys():
        print("session new ",request.session.get("nm"))
        a1=register.objects.get(email=request.session.get('nm'))
        a3=cart.objects.get(id=id)
        pro=productss.objects.get(brand=a3.name)
        a2=vendor.objects.get(fullname=a3.vendor)
        
        print("vendor",a2)
        print("user",a1)
        print("cart",a3)
        if 'submit1' in request.POST:
            quant=request.POST["qty"]
            price1=request.POST["totalprice"]
            
            val=buy123()
            val.user=a1
            val.vendor=a2
            val.name=a3
            val.quantity=quant
            val.totalprice=price1
            val.save()
            print("data saved")
            pro.quantity-=int(quant)
            pro.save()
            return redirect('address')
        else:
            messages.add_message(request, messages.ERROR, "Your data cannot save!")
            
        if 'submit2' in request.POST:
            a1.mobile=request.POST["mobile"]
            a1.address=request.POST["address"]
            a1.city=request.POST["city"]
            a1.save()
        else:
            pass
    return render(request,"buy.html",{'user1':a1,'h2':a2,'h3':a3})
    

def search(request,name):
    if request.session.keys():
        c1=subcategory.objects.get(name=name)
        p1=productss.objects.filter(subcate=c1)
        
        if request.POST:
            val=productss()
            val.subcate=p1
            val.save()        
    return render(request,"subcat.html",{'cat1':c1,'prod1':p1})

def myorder(request):
    if 'nm' in request.session.keys():
        a1=register.objects.get(email=request.session.get('nm'))
        a2=buy123.objects.filter(user=a1)
 
        
    return render(request,"myorder.html",{'user1':a1,'order':a2})


# ------------------------------------------------------------------------------

def vendorpro(request):
    if request.session.keys():
        h1=productss.objects.all()
        a1=vendor.objects.get(email=request.session.get('nm'))
        a2=subcategory.objects.all()   
        
        myList=[]
        if 'sub1' in request.POST:
            p1=request.POST["price"]
            p2=request.POST["price1"]
            print(p1,p2)
            for i in h1:
                if i.price>int(p1) and i.price<int(p2):
                    myList.append(i)
            return render(request,"pro.html",{'user1':a1,'data2':a2,'myList':myList})

        if 'sub2' in request.POST:
            print("hello")
            c1=subcategory.objects.get(name=request.POST["subcategory"])   
            p1=productss.objects.filter(subcate=c1)
                
            return render(request,'subcat.html',{'cat1':c1,'prod1':p1})
        
        return render(request,"vendor/vendorpro.html",{'data':h1,'user1':a1,'data2':a2})
    else:
        print("session not available")
        
def vendorbuy(request):
    if 'nm' in request.session.keys():
        a1=vendor.objects.get(email=request.session.get('nm'))
        
        hello=buy123.objects.filter(vendor=a1)

      
    return render(request,"vendor/vendorbuy.html",{'user1':a1,'buy':hello})

def menu(request):
    return render(request,"admin/adminmenu.html")

def detail(request,id):
    if 'nm' in request.session.keys():
        a1=vendor.objects.get(email=request.session.get('nm'))
        a2=buy123.objects.get(id=id)
          
    return render(request,"vendor/detail.html",{'user1':a1,'user':a2})

def view(request,id):
    if 'nm' in request.session.keys():
        a2=buy123.objects.get(id=id)
        m1=[]
       
            
        m1=a2.name.name.desc.split('.')
        
    return render(request,"vendor/vendorview.html",{'view':a2,'m1':m1})
def Venproview(request,id):
    if 'nm' in request.session.keys():
        a2=buy123.objects.get(id=id)
        m1=[]
       
            
        m1=a2.name.name.desc.split('.')
        
    return render(request,"venproview.html",{'view':a2,'m1':m1})

def Wallet(request):
    if 'nm' in request.session.keys():
        a1=vendor.objects.get(email=request.session.get('nm'))
        if request.POST:
            price1=request.POST['amount']
            valid=wallet()
            valid.vendor=a1
            valid.price=price1
            valid.save()
        return render(request,"vendor/wallet.html",{'user1':a1})
# -----------------------------------------------------------------------------------

def adregister(request):
    if request.method=="POST":
        fullname=request.POST["fullname"]
        email=request.POST["email"]
        dob=request.POST["dob"]		
        mobile=request.POST["mobile"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        city=request.POST["city"]
        password=request.POST["password"]
        upload1=request.FILES["upload"]
        
        request.session['pnm']=fullname       
         
        valid=admin1()
        valid.fullname=fullname
        valid.email=email
        valid.mobile=mobile
        valid.dob=dob
        valid.gender=gender
        valid.address=address
        valid.city=city
        valid.password=password
        valid.upload=upload1
        valid.save()
        return redirect("login")
    return render(request,"admin/adregister.html")

def adlogin(request):
    if request.POST:
        email1=request.POST["email"]
        Password1=request.POST["password"]
        n1=admin1.objects.get(email=email1)
        try:
            if n1:
                if n1.password == Password1:
                    request.session["nm"]=n1.email
                    
                    return redirect('showreg')

                else:
                    messages.add_message(request, messages.ERROR, "Your password does not match!!")
            else:
                messages.add_message(request, messages.ERROR, "Your email id does not match!!")
        except:
            messages.add_message(request, messages.ERROR, "Your email id does not match!!")
   
    return render(request,"admin/login.html")

def showreg(request):
    if 'nm' in request.session.keys():
        print("session",request.session.get('nm'))
        a2=admin1.objects.get(email=request.session.get('nm'))

        a1=register.objects.all()
     
   
    return render(request,'admin/registerdata.html',{'user1':a2,'reg':a1})

def Regedit(request,id):  
    if 'nm' in request.session.keys():
	    edit=register.objects.get(id=id)
	    if request.POST:
		    edit.fullname=request.POST['fullname']
		    edit.email=request.POST['email']
		    edit.mobile=request.POST['mobile']
		    edit.dob=request.POST['dob']
		    edit.gender=request.POST['gender']
		    edit.address=request.POST['address']
		    edit.city=request.POST['city']
		    edit.password=request.POST['password']
		    edit.upload=request.FILES['upload']
		    edit.save()
	    return render(request,"admin/regedit.html",{'editdata':edit})
def regdel(request,id):
    if 'nm' in request.session.keys():

        data=register.objects.get(id=id)
        data.delete()
    return redirect('showreg')

def addpro(request):
    if 'nm' in request.session.keys():
        print(request.session.get("nm"))
        # a1=register.objects.get(email=request.session.get('nm'))
        user=admin1.objects.get(email=request.session.get('nm'))

        
        h1=category.objects.all()
        h2=subcategory.objects.all()
        if request.POST:
            name1=request.POST["name"]
            brand1=request.POST["brand"]
            quantity1=request.POST["quantity"]
            price1=request.POST["price"]
            desc1=request.POST["desc"]
            image1=request.FILES["image"]
            a2=category.objects.get(name=request.POST['names'])
            a3=subcategory.objects.get(name=request.POST['cnames'])

            
            valid = productss(
                admin=user,
                cate=a2,
                subcate=a3,
                name=name1,
                price=price1,
                brand=brand1,
                quantity=quantity1,
                desc=desc1,
                image=image1,
            )
            
            valid.save()
            
            return render(request,"admin/addpro.html",{'cat':a2,'user2':a3,})

        return render(request,"admin/addpro.html",{'user1':user,'data':h1,'data2':h2,'data3':user})



    else:
        return redirect("login")
    return render(request,"admin/addpro.html")

def showpro(request):
    if 'nm' in request.session.keys():
        a22=admin1.objects.get(email=request.session.get('nm'))
        a1=productss.objects.all()
       
        
    return render(request,'admin/showpro.html',{'user1':a22,'pro':a1})

def prodel(request,id):
    if 'nm' in request.session.keys():

        data=productss.objects.get(id=id)
        data.delete()
    return redirect('showpro')

def adlogout(request):
    if "nm" in request.session:
        del request.session["nm"] 
        print("none")
        return redirect("ad1")
    else:
        pass

def proedit(request,id):  
    if 'nm' in request.session.keys():   
        a2=admin1.objects.get(email=request.session.get('nm'))
        c1=category.objects.all()
        c2=subcategory.objects.all()
        edit=productss.objects.get(id=id)
        if request.POST:
            c11=category.objects.get(name=request.POST['cate'])  
            c12=subcategory.objects.get(name=request.POST['subcate'])  
            edit.admin1=request.POST['admin']
            edit.brand1=request.POST['brand']
            edit.quanntity1=request.POST['quantity']
            edit.price1=request.POST['price']
            edit.desc1=request.POST['desc']
            edit.image=request.FILES['image']
            edit.cate=c11
            edit.subcate=c12
            if request.FILES.get('image') == None:
                pass
            else:
                edit.image=request.FILES["image"]
            edit.save()
            
            return redirect('showpro')
           
        return render(request,"admin/proedit.html",{'edit1':edit,'user1':a2,'cat':c1,'sub':c2,})

def showvendor(request):
    if 'nm' in request.session.keys():
        print("session",request.session.get('nm'))
        a2=admin1.objects.get(email=request.session.get('nm'))

        a1=vendor.objects.all()
     
   
    return render(request,'admin/showvendor.html',{'user1':a2,'vendor':a1})  

def vendordel(request,id):
    if 'nm' in request.session.keys():

        data=vendor.objects.get(id=id)
        data.delete()
    return redirect('showvendor')      

def showcate(request):
    if 'nm' in request.session.keys():
        print("session",request.session.get('nm'))
        a2=admin1.objects.get(email=request.session.get('nm'))

        a1=category.objects.all()
     
   
    return render(request,'admin/showcate.html',{'user1':a2,'cate':a1}) 

def catedel(request,id):
    if 'nm' in request.session.keys():

        data=category.objects.get(id=id)
        data.delete()
    return redirect('showcate')      
    
    
def cateedit(request,id):  
    if 'nm' in request.session.keys():
	    edit=category.objects.get(id=id)
	    if request.POST:
		    edit.name=request.POST['name']
		  
		    edit.save()
	    return render(request,"admin/cateedit.html",{'editdata':edit})
 
def addcate(request):
    a2=admin1.objects.get(email=request.session.get('nm'))

    if request.method=="POST":
        name=request.POST["name"]
        
        valid=category()
        valid.name=name
        valid.save()
    return render(request,"admin/addcate.html",{'user1':a2})

def showsub(request):
    if 'nm' in request.session.keys():
        print("session",request.session.get('nm'))
        a2=admin1.objects.get(email=request.session.get('nm'))

        a1=subcategory.objects.all()
    return render(request,'admin/showsub.html',{'user1':a2,'sub':a1}) 



def subdel(request,id):
    if 'nm' in request.session.keys():

        data=subcategory.objects.get(id=id)
        data.delete()
    return redirect('showsub')      
    
    

 
def addsub(request):
    if 'nm' in request.session.keys():
        a1=category.objects.all()
        a2=admin1.objects.get(email=request.session.get('nm'))
        if request.method=="POST":
            name=request.POST["name"]
            c1=category.objects.get(name=request.POST['cname'])  
            
            valid=subcategory()
            valid.cname=c1
            valid.name=name
            valid.save()
            return render(request,"admin/addsub.html",{'cat':c1})
        return render(request,"admin/addsub.html",{'user1':a2,'cat1':a1})
    
def subedit(request,id):  
    if 'nm' in request.session.keys():   
        a2=admin1.objects.get(email=request.session.get('nm'))
        c1=category.objects.all()
        edit=subcategory.objects.get(id=id)
        if request.POST:
            c11=category.objects.get(name=request.POST['cname'])   
            edit.name=request.POST['name']
            edit.cname=c11
            
            edit.save()
            return redirect('showsub')
        return render(request,"admin/subedit.html",{'edit1':edit,'user1':a2,'cat':c1})
    
    
def showcart(request):
     if 'nm' in request.session.keys():   
        a2=admin1.objects.get(email=request.session.get('nm'))
        
        c1=cart.objects.all()
        return render(request,"admin/showcart.html",{'cart':c1,'user1':a2})
    
def cartdel(request,id):
    if 'nm' in request.session.keys():
        a2=admin1.objects.get(email=request.session.get('nm'))
        
        c1=cart.objects.get(id=id)
        c1.delete()
        return redirect('showcart')
    
def cartedit(request,id):  
    if 'nm' in request.session.keys():   
        a2=admin1.objects.get(email=request.session.get('nm'))
        c1=register.objects.all()
        c2=productss.objects.all()
        c3=vendor.objects.all()
        edit=cart.objects.get(id=id)
        if request.POST:
            c11=register.objects.get(fullname=request.POST['reg']) 
            c12=productss.objects.get(brand=request.POST['pro'])   
            c13=vendor.objects.get(fullname=request.POST['vendor'])
            edit.user=c11  
            edit.name=c12
            edit.vendor=c13
            edit.save()
            
            return redirect('showcart')
        return render(request,"admin/cartedit.html",{'cart1':edit,'user1':a2,'reg':c1,'pro':c2,'vendor':c3})

def showbuy(request):
    if 'nm' in request.session.keys():   
        a2=admin1.objects.get(email=request.session.get('nm'))
        
        b1=buy123.objects.all()
        return render(request,"admin/showbuy.html",{'buy':b1,'user1':a2})
    
def buydel(request,id):
    if 'nm' in request.session.keys():
        a2=admin1.objects.get(email=request.session.get('nm'))
        
        c1=buy123.objects.get(id=id)
        c1.delete()
        return redirect('showbuy')
    
def buyedit(request,id):  
    if 'nm' in request.session.keys():   
        a2=admin1.objects.get(email=request.session.get('nm'))
        c1=register.objects.all()
        c2=cart.objects.all()
        c3=vendor.objects.all()
        edit=buy123.objects.get(id=id)
        if request.POST:
            c11=register.objects.get(fullname=request.POST['reg'])
            print("id",request.POST.get('pro')) 
            c12=cart.objects.get(id=request.POST['pro'])   
            c13=vendor.objects.get(fullname=request.POST['vendor'])
            edit.quantity=request.POST['quantity']
            edit.price=request.POST['price']
            edit.user=c11  
            edit.name=c12
            edit.vendor=c13
            edit.save()
            
            return redirect('showbuy')
        return render(request,"admin/buyedit.html",{'buy1':edit,'user1':a2,'reg':c1,'cart':c2,'vendor':c3})

def City(request):
    if 'nm' in request.session.keys():   
        c1=city.objects.all()
        c2=country.objects.all()
        c3=state.objects.all()
        if 'ct' in request.POST:
            check1=country.objects.get(country=request.POST['country'])
            stat=state.objects.filter(count=check1)
            return render(request,'admin/city.html',{'city':c1,'check':check1,'stat':stat})
        if 'st' in request.POST:
            s1=state.objects.get(state=request.POST['state'])
            cit=city.objects.filter(stat=s1)
            return render(request,'admin/city.html',{'city':cit,'country':c2,'state1':s1})
        return render(request,'admin/city.html',{'city':c1,'country':c2,'stat':c3})
 
def vendoredit1(request,id):  
    if 'nm' in request.session.keys():
	    edit=vendor.objects.get(id=id)
	    if request.POST:
		    edit.fullname=request.POST['fullname']
		    edit.email=request.POST['email']
		    edit.mobile=request.POST['mobile']
		    edit.dob=request.POST['dob']
		    edit.gender=request.POST['gender']
		    edit.address=request.POST['address']
		    edit.city=request.POST['city']
		    edit.password=request.POST['password']
		    edit.upload=request.FILES['upload']
		    edit.save()
	    return render(request,"admin/vendoredit.html",{'editdata':edit}) 
def Voucher(request,id):
    if 'nm' in request.session.keys():

        a3=buy123.objects.get(id=id)
        a2=register.objects.get(fullname=a3.user)
        a1=vendor.objects.get(fullname=a3.vendor)
        a4=wallet.objects.get(vendor=a1)

        p1=a3.name.name.quantity
        A=a3.quantity
        print("sum",(p1+A))
        a3.name.name.quantity=(p1+A)
        a3.save()
        val=voucher()
        val.user=a2
        val.vendor=a1
        val.buy=a3
        val.wallet=a4
        val.save()
        a4.price-=int(a3.totalprice)
        a4.save()
        
        
        return redirect('ref')
    
def showrefund(request):
    if 'nm' in request.session.keys():
        v1=voucher.objects.all()
    
    return render(request,"vendor/voucher.html",{'vou':v1})

def refundview(request,id):
    if 'nm' in request.session.keys():
        a2=vendor.objects.get(email=request.session.get('nm'))

        v1=voucher.objects.get(id=id)
     
    
    return render(request,"refundview.html",{'vou':v1,'user1':a2})

def ref(request):
    return render(request,'refund.html')



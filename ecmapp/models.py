from django.db import models

# Create your models here.
class register(models.Model):
	fullname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.IntegerField()
	dob=models.CharField(max_length=10)
	gender=models.CharField(max_length=10)
	address=models.CharField(max_length=500)
	city=models.CharField(max_length=10)
	password=models.CharField(max_length=12) 
	upload=models.FileField(upload_to='documents/', max_length=255, null=True, blank=True)


	def __str__(self):
		return self.fullname

class product(models.Model):
    Aname=models.ForeignKey(register,on_delete=models.CASCADE,default="")
    pname=models.CharField(max_length=100)
    pquantity=models.IntegerField()
    pprice=models.IntegerField()
    pdesc = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to="media/", null=True)

    
    def __str__(self):
        return self.pname
    
class person(models.Model):
    age=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name.pname
    
class category(models.Model):
    name=models.CharField(max_length=100, null=True,blank=True)
        
    def __str__(self):
        return self.name
    
class subcategory(models.Model):
    name=models.CharField(max_length=100, null=True,blank=True)
    cname=models.ForeignKey(category,on_delete=models.CASCADE,default="")
    
    def __str__(self):
        return self.name
    
class vendor(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.IntegerField()
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=10)
    password=models.CharField(max_length=12)
    upload=models.FileField(upload_to='documents/', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.fullname
    
class productss(models.Model):
    cate=models.ForeignKey(category,on_delete=models.CASCADE,default="")
    subcate=models.ForeignKey(subcategory,on_delete=models.CASCADE,default="")
    admin=models.ForeignKey(vendor,on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.IntegerField()
    desc=models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/", null=True)
    
    def __str__(self):
        return self.brand
    

    
class cart(models.Model):
    user=models.ForeignKey(register,on_delete=models.CASCADE,default="")
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE,default="")
    name=models.ForeignKey(productss,on_delete=models.CASCADE,default="")
    
    def __str__(self):
        return self.user.fullname
    
class address(models.Model):
    fname=models.CharField(max_length=100)
    mobile=models.IntegerField()
    home_no=models.CharField(max_length=10)
    landmark=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    pincode=models.IntegerField()
    state=models.CharField(max_length=20)
    type=models.CharField(max_length=30)
    
    
class buy123(models.Model):
    user=models.ForeignKey(register,on_delete=models.CASCADE,default="")
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE,default="")
    name=models.ForeignKey(cart,on_delete=models.CASCADE,default="")
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
    
    
    def __str__(self):
        return self.user.fullname+"->"+self.name.name.name
    
class admin1(models.Model):
	fullname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.IntegerField()
	dob=models.CharField(max_length=10)
	gender=models.CharField(max_length=10)
	address=models.CharField(max_length=500)
	city=models.CharField(max_length=10)
	password=models.CharField(max_length=12)
	upload=models.FileField(upload_to='documents/', max_length=255, null=True, blank=True)


	def __str__(self):
		return self.fullname

class country(models.Model):
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.country
    
class state(models.Model):
    state=models.CharField(max_length=100)
    count=models.ForeignKey(country,on_delete=models.CASCADE,default="")
    
    def __str__(self):
        return self.state
class city(models.Model):
    city=models.CharField(max_length=100)
    count=models.ForeignKey(country,on_delete=models.CASCADE,default="")
    stat=models.ForeignKey(state,on_delete=models.CASCADE,default="")
    
    def __str__(self):
        return self.city
    
class wallet(models.Model):
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE,default="")
    price=models.IntegerField()
    
    def __str__(self):
        return self.vendor.fullname

class voucher(models.Model):
    user=models.ForeignKey(register,on_delete=models.CASCADE,default="")
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE,default="")
    buy=models.ForeignKey(buy123,on_delete=models.CASCADE,default="")
    wallet=models.ForeignKey(wallet,on_delete=models.CASCADE,default="")
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vendor.fullname

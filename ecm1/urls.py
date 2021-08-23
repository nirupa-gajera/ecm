"""ecm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecmapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('reg/',views.Register,name="reg"),
    path("login/",views.login,name="login"),
    path('show/',views.show,name="show"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('download/<int:id>',views.download,name="download"),
    path("email/", views.email, name="email"),
    path("otp/",views.send_otp,name="otp"),
    path("ocheck/",views.otpcheck,name="ocheck"),
    path("password/",views.Password,name="password"),
    path('rename/<int:id>',views.Rename,name="rename"),
    path('product/',views.Product,name="product"),
    path('logout/',views.logout,name="logout"),
    path('pro/',views.pro,name="pro"),
    path('cat/',views.categories,name="cat"),
    path('cart/<int:id>',views.cart1,name="cart"),
    path('Add_cart/<int:id>',views.Add_cart,name="Add_cart"),
    path('Show_cart/',views.Show_cart,name="Show_cart"), 
    path("address/",views.Address,name="address"),    
    path('buy/<int:id>',views.Buy,name="buy"),
    path('search/<str:name>',views.search,name="search"),    
    path("autocomplete/",views.autocomplete,name="autocomplete"),
    path('myorder/',views.myorder,name="myorder"),
    path('ref/',views.ref,name="ref"),
    path('voucher/<int:id>',views.Voucher,name="voucher"),
    path('venproview/<int:id>',views.Venproview,name="venproview"), 
    path('refundview/<int:id>',views.refundview,name="refundview"), 


    
    path('vendor/',views.Admin,name="vendor"),
    path("adlogin/",views.adminlogin,name="adlogin"),    
    path("adminlogout/",views.adminlogout,name="adminlogout"),  
    path("vendorpro/",views.vendorpro,name="vendorpro"),
    path('vendorbuy/',views.vendorbuy,name="vendorbuy"),
    path('menu/',views.menu,name="menu"),
    path('wallet/',views.Wallet,name="wallet"),
    path('detail/<int:id>',views.detail,name="detail"),
    path('view/<int:id>',views.view,name="view"),
    path('showrefund/',views.showrefund,name="showrefund"),


    
    path('ad1/',views.adregister,name="ad1"),
    path("log/",views.adlogin,name="log"), 
    path("showreg/",views.showreg,name="showreg"),    
    path("regedit/<int:id>",views.Regedit,name="regedit"),    
    path('regdel/<int:id>',views.regdel,name="regdel"),
    path('addpro/',views.addpro,name="addpro"),
    path("showpro/",views.showpro,name="showpro"), 
    path('prodel/<int:id>',views.prodel,name="prodel"),
    path("adlogout/",views.adlogout,name="adlogout"),
    path("proedit/<int:id>",views.proedit,name="proedit"),
    path("showvendor/",views.showvendor,name="showvendor"),        
    path('vendordel/<int:id>',views.vendordel,name="vendordel"),
    path("vendoredit/<int:id>",views.vendoredit1,name="vendoredit"),   
    path("showcate/",views.showcate,name="showcate"),        
    path('catedel/<int:id>',views.catedel,name="catedel"),
    path("cateedit/<int:id>",views.cateedit,name="cateedit"),  
    path('addcate/',views.addcate,name="addcate"),
    path("showsub/",views.showsub,name="showsub"),        
    path('subdel/<int:id>',views.subdel,name="subdel"),
    path('addsub/',views.addsub,name="addsub"),
    path("subedit/<int:id>",views.subedit,name="subedit"),
    path("showcart/",views.showcart,name="showcart"), 
    path('cartdel/<int:id>',views.cartdel,name="cartdel"),
    path("cartedit/<int:id>",views.cartedit,name="cartedit"),
    path("showbuy/",views.showbuy,name="showbuy"),        
    path('buydel/<int:id>',views.buydel,name="buydel"),
    path("buyedit/<int:id>",views.buyedit,name="buyedit"),
    path('city/',views.City,name="City"),
    path('admin/', admin.site.urls),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

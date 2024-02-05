from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import userform
from product.models import Product
from django.contrib.auth.models import User



def aboutUs(request):
    return render(request,"aboutus.html")



def productDetails(request,productid):
    return HttpResponse(f"view this product {productid}")
def homepage(request):
    data={
        'title':'BabyBedding'
    }
    return render(request,"index.html",data) 

def product(request):

    product_data=Product.objects.all()
    data={
        'product_data':product_data
    }
    return render( request,"product.html",data)

def contact(request):
    form=userform()
    return render(request,"contact.html",{'form':form})


def signup(request):
    

    if request.method =="POST":
            uname=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password1')
            confirm_password=request.POST.get('password2')
            if confirm_password!=password:
                 data={
                      'message':'Password donot match'
                 }
                 return render(request,"signup.html",data)
            else:
                my_user=User.objects.create_user(uname,email,password)
                my_user.save()
                return redirect("/signup")

   

    return render(request,"signup.html")
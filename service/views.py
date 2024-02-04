from django.http import HttpResponse
from django.shortcuts import render


from .forms import userform




def aboutUs(request):
    return render(request,"aboutus.html")



def productDetails(request,productid):
    return HttpResponse(f"view this product {productid}")
def homepage(request):
    data={
        'title':'BabyBedding'
    }
    return render(request,"index.html",data) 


def contact(request):
    form=userform()
    return render(request,"contact.html",{'form':form})

def userForm(request):
    form=userform()
    return render(request,"userform.html",{'form': form})
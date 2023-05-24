from django.shortcuts import render

# Create your views here.

def jinjaprint(request):
    d={'name':'abi'}
    return render(request,'jinja_print.html',context=d)

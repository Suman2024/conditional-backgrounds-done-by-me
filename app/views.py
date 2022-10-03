from django.shortcuts import render

# Create your views here.
def manith(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'mani.html',context=d)
from django.shortcuts import render

# Create your views here.

def payement_done(request):
    return render(request,'payement/done.html')


def payement_canceled(request):
    return render(request,'payement/canceled.html')
from django.shortcuts import render

def sore(request):
    return render(request, 'store/store.html')

from django.shortcuts import render

# Create your views here.
def show_main(request):
    return render(request, "cek-royalti.html")
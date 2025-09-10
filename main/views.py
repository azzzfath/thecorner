from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406412152',
        'name': 'Muhammad Azzam Fathurrahman',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
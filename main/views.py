from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Maira Azma Shaliha',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
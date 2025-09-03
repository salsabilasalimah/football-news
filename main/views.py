from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406432734',
        'name': 'Salsabila Salimah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.

from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Gooner Store',
        'name' : 'Julius Albert Wirayuda',
        'class' : 'PBP F',
    }

    return render(request, "main.html", context)
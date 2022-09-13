from django.shortcuts import render

def index_view(request):
    return render(request, 'user_app/index.html')

def register_view(request):
    return render(request, 'user_app/register_page.html')
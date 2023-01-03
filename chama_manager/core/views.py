from django.shortcuts import render

# Render Homepage
def index(request):
    return render(request, 'core/index.html')

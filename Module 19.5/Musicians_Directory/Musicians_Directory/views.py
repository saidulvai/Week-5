from django.shortcuts import render
from Album.models import Album
def viewinfo(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'data': data})
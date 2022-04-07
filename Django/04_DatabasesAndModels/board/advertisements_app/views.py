from django.shortcuts import render
from advertisements_app.models import Advertisement


def advertisement(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisements_app/advertisement.html', {'advertisement': advertisements})

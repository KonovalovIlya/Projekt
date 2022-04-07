from django.shortcuts import render
from advertisements_app.models import Advertisement
from django.views import generic


# def advertisement(request, *args, **kwargs):
#     advertisements = Advertisement.objects.all()
#     return render(request, 'advertisements_app/advertisement1.html', {'advertisements': advertisements})


class AdvertisementsListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisement_detail.html'
from django.shortcuts import render
from advertisements_app.models import Advertisement
from django.views import generic, View
from advertisements_app.forms import AdvertisementForm
from django.http import HttpResponseRedirect


# def advertisement(request, *args, **kwargs):
#     advertisements = Advertisement.objects.all()
#     return render(request, 'advertisements_app/advertisement1.html', {'advertisements': advertisements})


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisement_detail.html'


class AdvertisementFormView(View):

    def get(self, request):
        advertisement_form = AdvertisementForm()
        return render(request, 'advertisements/advertisement_form.html', {'advertisement_form': advertisement_form})

    def post(self, request):
        advertisement_form = AdvertisementForm(request.POST)

        if advertisement_form.is_valid():
            Advertisement.objects.create(**advertisement_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'advertisements/advertisement_form.html', {'advertisement_form': advertisement_form})


class AdvertisementFormEditView(View):
    def get(self, request, profile_id):
        advertisement = Advertisement.objects.get(id=profile_id)
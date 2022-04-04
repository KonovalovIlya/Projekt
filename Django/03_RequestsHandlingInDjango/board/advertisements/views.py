from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from advertisements.models import Advertisement



def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})


class Advertisements(View):
    def get(self, request):
        self.list_ = [
            'Мастер на час - 500 в час',
            'Выведение из запоя - 1000 за сеанс',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура - 1500 в час'
            'Продам почку за тарелку супа'
        ]
        return render(request, 'advertisements/advertisements.html', {'advertisements': self.list_})

    def post(self, request):
        return 'Запрос на создание новой записи успешно выполнен.'


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'г. Москва'
        context['phone_number'] = '89876543212'
        context['e_mail'] = 'example@example.com'
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О компании"'
        context['name'] = 'ООО "Рога и копыта"'
        context['info'] = 'Здесь описание компании'
        return context


class MainPage(View):

    def get(self, request):
        categories = ['Электроника', 'Бытовая техника', 'Телевизоры']
        cities = ['Москва', 'Нижний Новгород', 'Киров']

        return render(request, 'advertisements/main_page.html', {'categories': categories, 'cities': cities})

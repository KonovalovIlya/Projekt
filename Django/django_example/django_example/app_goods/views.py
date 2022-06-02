from _csv import reader
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render
from app_goods.models import Item
from app_goods.forms import UploadPriceForm


def items_list(request):
    items = Item.objects.all()
    return render(request, 'goods/items_list.html', {'items_list': items})


def upload_price(request):
    if request.method == 'POST':
        upload_price_form = UploadPriceForm(request.POST, request.FILES)
        if upload_price_form.is_valid():
            price_file = upload_price_form.cleaned_data['file'].read()
            price_string = price_file.decode('utf-8').split('\n')
            csv_reader = reader(price_string, delimiter=':', quotechar='"')
            for row in csv_reader:
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            return HttpResponse(content='Цены были успешно обновлены', status=200)
    else:
        upload_price_form = UploadPriceForm()
    return render(request, 'goods/upload_price_file.html', context={'form': upload_price_form})

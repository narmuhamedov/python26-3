from django.shortcuts import render, get_object_or_404
from . import models

#не полная информация о товаре
def phone_list_view(request):
    phone_object = models.PhoneShop.objects.all()
    return render(request, 'phone_list.html', {'phone_object': phone_object})


#Полная информация об объекте по id
def phone_detail_view(request, id):
    phone_detail = get_object_or_404(models.PhoneShop, id=id)
    return render(request, 'phone_detail.html', {'phone_detail': phone_detail})


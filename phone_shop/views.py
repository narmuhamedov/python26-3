from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

#не полная информация о товаре
def phone_list_view(request):
    phone_object = models.PhoneShop.objects.all()
    return render(request, 'phone_list.html', {'phone_object': phone_object})


#Полная информация об объекте по id
def phone_detail_view(request, id):
    phone_detail = get_object_or_404(models.PhoneShop, id=id)
    return render(request, 'phone_detail.html', {'phone_detail': phone_detail})

#создание объектов через формы
def create_object_view(request):
    method = request.method
    if method == "POST":
        form = forms.PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Успешно добавлен в Базу Данных")
    else:
        form = forms.PhoneForm()
    return render(request, "create_phone.html", {'form': form})

#Удаление из базы
def delete_object_view(request, id):
    phone_object = get_object_or_404(models.PhoneShop, id=id)
    phone_object.delete()
    return HttpResponse('Телефон удален из Базы данных')

#Редактирование
def update_object_view(request, id):
    phone_object = get_object_or_404(models.PhoneShop, id=id)
    if request.method == 'POST':
        form = forms.PhoneForm(instance=phone_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно обновлены')
    else:
        form = forms.PhoneForm(instance=phone_object)

    context = {
        'form': form,
        'object': phone_object
    }
    return render(request, 'update_phone.html', context)

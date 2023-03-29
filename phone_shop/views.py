from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

#не полная информация о товаре
class PhoneListView(ListView):
    template_name = 'phone_list.html'
    queryset = models.PhoneShop.objects.all()
    def get_queryset(self):
        return models.PhoneShop.objects.all()

# def phone_list_view(request):
#     phone_object = models.PhoneShop.objects.all()
#     return render(request, 'phone_list.html', {'phone_object': phone_object})


#Полная информация об объекте по id

class PhoneDetailView(DetailView):
    template_name = 'phone_detail.html'
    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.PhoneShop, id=phone_id)


# def phone_detail_view(request, id):
#     phone_detail = get_object_or_404(models.PhoneShop, id=id)
#     return render(request, 'phone_detail.html', {'phone_detail': phone_detail})

#создание объектов через формы

class CreatePhoneView(CreateView):
    template_name = 'create_phone.html'
    form_class = forms.PhoneForm
    queryset = models.PhoneShop.objects.all()
    success_url = '/phone_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePhoneView, self).form_valid(form=form)


# def create_object_view(request):
#     method = request.method
#     if method == "POST":
#         form = forms.PhoneForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Успешно добавлен в Базу Данных")
#     else:
#         form = forms.PhoneForm()
#     return render(request, "create_phone.html", {'form': form})

#Удаление из базы

class PhoneDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/phone_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.PhoneShop, id=phone_id)

# def delete_object_view(request, id):
#     phone_object = get_object_or_404(models.PhoneShop, id=id)
#     phone_object.delete()
#     return HttpResponse('Телефон удален из Базы данных')

#Редактирование
class PhoneUpdateView(UpdateView):
    template_name = 'update_phone.html'
    form_class = forms.PhoneForm
    success_url = '/phone_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.PhoneShop, id=phone_id)

    def form_valid(self, form):
        return super(PhoneUpdateView, self).form_valid(form=form)


# def update_object_view(request, id):
#     phone_object = get_object_or_404(models.PhoneShop, id=id)
#     if request.method == 'POST':
#         form = forms.PhoneForm(instance=phone_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Данные успешно обновлены')
#     else:
#         form = forms.PhoneForm(instance=phone_object)
#
#     context = {
#         'form': form,
#         'object': phone_object
#     }
#     return render(request, 'update_phone.html', context)

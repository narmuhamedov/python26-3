from django.db import models

class PhoneShop(models.Model):
    PHONE_TYPE = (
        ('Для школьников', "Для школьников"),
        ("Для студентов и взрослых", "Для студентов и взрослых"),
        ("Для пенсионеров", "Для пенсионеров")
    )
    title = models.CharField("Название телефона", max_length=100)
    description = models.TextField("Описание телефона")
    image = models.ImageField(upload_to='')
    phone_type = models.CharField(max_length=100, choices=PHONE_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()

    def __str__(self):
        return self.title

# Generated by Django 4.1.7 on 2023-03-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

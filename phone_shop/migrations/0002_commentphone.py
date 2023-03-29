# Generated by Django 4.1.7 on 2023-03-29 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rate_stars', models.CharField(choices=[('*', '*'), ('**', '**'), ('***', '***'), ('****', '****'), ('*****', '*****')], max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('phone_choice_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='phone_shop.phoneshop')),
            ],
        ),
    ]

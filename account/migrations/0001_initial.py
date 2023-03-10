# Generated by Django 4.0.6 on 2022-08-22 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='dumy',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_history',
            fields=[
                ('Search_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Search_query', models.CharField(max_length=50)),
                ('search_result', models.CharField(max_length=50)),
                ('search_date', models.DateField(auto_now_add=True)),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

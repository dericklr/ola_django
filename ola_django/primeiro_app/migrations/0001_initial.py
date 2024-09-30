# Generated by Django 5.1.1 on 2024-09-30 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('idade', models.IntegerField()),
                ('email', models.CharField(max_length=60)),
            ],
        ),
    ]

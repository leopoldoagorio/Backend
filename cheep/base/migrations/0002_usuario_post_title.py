# Generated by Django 4.1.5 on 2023-01-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Titulo', max_length=200),
            preserve_default=False,
        ),
    ]

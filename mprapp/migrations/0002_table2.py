# Generated by Django 3.2.5 on 2021-07-29 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=400)),
            ],
        ),
    ]

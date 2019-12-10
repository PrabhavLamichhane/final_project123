# Generated by Django 2.1.4 on 2019-12-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='homeSlide')),
                ('text1', models.CharField(blank=True, max_length=200, null=True)),
                ('text2', models.CharField(blank=True, max_length=200, null=True)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
    ]

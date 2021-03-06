# Generated by Django 3.2.6 on 2021-09-14 08:12

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20210820_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='body',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=64, verbose_name='비밀번호'),
        ),
    ]

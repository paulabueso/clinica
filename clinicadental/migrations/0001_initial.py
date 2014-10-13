# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MakeAppointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=9, validators=[django.core.validators.RegexValidator(regex=b'^\\d{9}$', message=b'Debe tener 9 digitos', code=b'numero invalido')])),
                ('email', models.EmailField(max_length=70)),
                ('dr', models.CharField(max_length=200, choices=[(b'Dra Ana Bejar', b'Dra. Ana Bejar'), (b'Dra Maria LLerandi', b'Dra. Maria LLerandi')])),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=200, choices=[(b'9:00', b'9:00'), (b'9.30', b'9:30'), (b'10.00', b'10:00'), (b'10:30', b'10:30'), (b'11:00', b'11:00'), (b'11:30', b'11:30'), (b'12:00', b'12:00'), (b'12:30', b'12:30'), (b'13:00', b'13:00'), (b'13:30', b'13:30'), (b'14:00', b'14:00'), (b'14:30', b'14:30'), (b'15:00', b'15:00'), (b'15:30', b'15:30'), (b'16:00', b'16:00'), (b'16:30', b'16:30'), (b'17:00', b'17:00')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

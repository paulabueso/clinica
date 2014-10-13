# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicadental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeappointment',
            name='dr',
            field=models.CharField(max_length=200, choices=[(b'Dra Ana Bejar', b'Dra. Ana Bejar'), (b'Dra Maria LLerandi', b'Dra. Maria LLerandi'), (b'no especificado', b'No lo se')]),
        ),
    ]

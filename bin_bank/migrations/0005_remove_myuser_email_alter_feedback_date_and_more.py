# Generated by Django 4.1 on 2022-10-28 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bin_bank', '0004_alter_feedback_date_alter_transaction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='email',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 23, 34, 13, 258584, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 28, 23, 34, 13, 257570, tzinfo=datetime.timezone.utc)),
        ),
    ]

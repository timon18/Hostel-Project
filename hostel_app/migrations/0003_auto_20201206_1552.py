# Generated by Django 3.1.3 on 2020-12-06 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0002_reservation_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_app.profile'),
        ),
    ]

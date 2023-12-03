# Generated by Django 4.2.7 on 2023-12-02 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_cliente_cliente_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cliente_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

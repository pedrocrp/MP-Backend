# Generated by Django 4.2.7 on 2023-12-02 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cliente_user',
        ),
    ]

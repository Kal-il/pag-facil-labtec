# Generated by Django 5.1.3 on 2024-12-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamentos', '0002_documentoboleto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoboleto',
            name='arquivo',
            field=models.FileField(upload_to='solicitacoes/'),
        ),
    ]
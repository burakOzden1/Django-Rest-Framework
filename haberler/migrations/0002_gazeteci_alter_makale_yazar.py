# Generated by Django 5.0.3 on 2024-03-26 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gazeteci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=120)),
                ('soyisim', models.CharField(max_length=120)),
                ('biyografi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='makale',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makaleler', to='haberler.gazeteci'),
        ),
    ]

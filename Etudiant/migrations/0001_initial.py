# Generated by Django 2.2 on 2019-04-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=30)),
                ('matricule', models.CharField(max_length=8)),
                ('adresse', models.CharField(max_length=20)),
                ('option', models.CharField(max_length=30)),
                ('niveau', models.CharField(max_length=5)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]

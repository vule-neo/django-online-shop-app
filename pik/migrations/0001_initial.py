# Generated by Django 3.0.3 on 2020-03-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(choices=[('i', 'Iznos'), ('p', 'Po dogovoru')], max_length=1)),
                ('category', models.CharField(choices=[('A', 'Vozila'), ('B', 'Namještaj'), ('C', 'Bela tehnika'), ('D', 'Odjeća'), ('E', 'Tehnologija'), ('F', 'Igračke'), ('G', 'Literatura'), ('H', 'Nekretnine'), ('I', 'Ostalo')], max_length=1)),
                ('description', models.TextField(max_length=300)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('replacement', models.BooleanField()),
            ],
        ),
    ]

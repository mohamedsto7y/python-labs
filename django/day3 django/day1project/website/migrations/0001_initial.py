# Generated by Django 4.1.6 on 2023-02-06 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('blog_text', models.TextField()),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.category')),
            ],
        ),
    ]

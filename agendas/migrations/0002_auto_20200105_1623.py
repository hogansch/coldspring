# Generated by Django 2.2.9 on 2020-01-05 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('agendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name='Agenda PDF'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='date',
            field=models.DateField(verbose_name='Date of Meeting'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_log_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('comment', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-09-05 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
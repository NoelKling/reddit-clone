# Generated by Django 3.2.5 on 2021-07-15 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_alter_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='mptt_level',
            new_name='level',
        ),
    ]
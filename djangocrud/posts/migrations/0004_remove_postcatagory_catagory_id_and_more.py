# Generated by Django 4.1.4 on 2023-01-11 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcatagory',
            name='catagory_id',
        ),
        migrations.RemoveField(
            model_name='postcatagory',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='tag_id',
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostCatagory',
        ),
        migrations.DeleteModel(
            name='PostTag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]

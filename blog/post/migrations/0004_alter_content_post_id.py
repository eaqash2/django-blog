# Generated by Django 4.1.5 on 2024-02-27 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_content_remove_post_content_image_content_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='post_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='post_id'),
        ),
    ]
# Generated by Django 4.2.9 on 2024-02-18 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(default='be18eb8b-9b82-4bc4-be01-cef68b07eeb7', on_delete=django.db.models.deletion.DO_NOTHING, to='core.usertype'),
            preserve_default=False,
        ),
    ]
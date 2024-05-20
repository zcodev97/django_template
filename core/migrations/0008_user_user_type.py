# Generated by Django 4.2.9 on 2024-02-26 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(default='0d1bf7e3-5610-4650-8804-46ee810e20b2', on_delete=django.db.models.deletion.CASCADE, to='core.usertype'),
            preserve_default=False,
        ),
    ]

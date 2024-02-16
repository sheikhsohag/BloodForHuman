# Generated by Django 5.0.1 on 2024-02-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location_track',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
# Generated by Django 2.1.7 on 2019-03-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190302_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sapfile',
            old_name='sample_SAP',
            new_name='Card_SAP',
        ),
        migrations.AddField(
            model_name='sapfile',
            name='Cheque_SAP',
            field=models.FileField(default=0, upload_to='SAP/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sapfile',
            name='OCR_image',
            field=models.ImageField(default=0, upload_to='OCR/'),
            preserve_default=False,
        ),
    ]
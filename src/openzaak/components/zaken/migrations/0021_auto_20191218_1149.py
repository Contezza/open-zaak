# Generated by Django 2.2.4 on 2019-12-18 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalogi", "0016_auto_20191204_1500"),
        ("zaken", "0020_auto_20191220_1029"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resultaat", old_name="resultaattype", new_name="_resultaattype"
        ),
        migrations.AddField(
            model_name="resultaat",
            name="_resultaattype_url",
            field=models.URLField(
                blank=True,
                help_text="URL-referentie naar extern RESULTAATTYPE (in een andere Catalogi API).",
                max_length=1000,
                verbose_name="extern resultaattype",
            ),
        ),
    ]
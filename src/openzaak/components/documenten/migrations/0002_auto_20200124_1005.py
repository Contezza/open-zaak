# Generated by Django 2.2.9 on 2020-01-24 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documenten', '0001_initial'),
        ('catalogi', '0001_initial'),
        ('zaken', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectinformatieobject',
            name='_zaak',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zaken.Zaak'),
        ),
        migrations.AddField(
            model_name='objectinformatieobject',
            name='informatieobject',
            field=models.ForeignKey(help_text='URL-referentie naar het INFORMATIEOBJECT.', on_delete=django.db.models.deletion.CASCADE, to='documenten.EnkelvoudigInformatieObjectCanonical'),
        ),
        migrations.AddField(
            model_name='gebruiksrechten',
            name='informatieobject',
            field=models.ForeignKey(help_text='URL-referentie naar het INFORMATIEOBJECT.', on_delete=django.db.models.deletion.CASCADE, to='documenten.EnkelvoudigInformatieObjectCanonical'),
        ),
        migrations.AddField(
            model_name='enkelvoudiginformatieobject',
            name='_informatieobjecttype',
            field=models.ForeignKey(blank=True, help_text='URL-referentie naar het INFORMATIEOBJECTTYPE (in de Catalogi API).', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogi.InformatieObjectType'),
        ),
        migrations.AddField(
            model_name='enkelvoudiginformatieobject',
            name='canonical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documenten.EnkelvoudigInformatieObjectCanonical'),
        ),
        migrations.AddConstraint(
            model_name='objectinformatieobject',
            constraint=models.CheckConstraint(check=models.Q(models.Q(models.Q(models.Q(('_zaak__isnull', False), ('_zaak_url', '')), models.Q(models.Q(_negated=True, _zaak_url=''), ('_zaak__isnull', True)), _connector='OR'), ('_besluit__isnull', True), ('_besluit_url', ''), ('object_type', 'zaak')), models.Q(models.Q(models.Q(('_besluit__isnull', False), ('_besluit_url', '')), models.Q(models.Q(_besluit_url='', _negated=True), ('_besluit__isnull', True)), _connector='OR'), ('_zaak__isnull', True), ('_zaak_url', ''), ('object_type', 'besluit')), _connector='OR'), name='check_type'),
        ),
        migrations.AddConstraint(
            model_name='objectinformatieobject',
            constraint=models.UniqueConstraint(fields=('informatieobject', '_zaak'), name='unique_io_zaak_local'),
        ),
        migrations.AddConstraint(
            model_name='objectinformatieobject',
            constraint=models.UniqueConstraint(condition=models.Q(_negated=True, _zaak_url=''), fields=('informatieobject', '_zaak_url'), name='unique_io_zaak_external'),
        ),
        migrations.AddConstraint(
            model_name='objectinformatieobject',
            constraint=models.UniqueConstraint(fields=('informatieobject', '_besluit'), name='unique_io_besluit_local'),
        ),
        migrations.AddConstraint(
            model_name='objectinformatieobject',
            constraint=models.UniqueConstraint(condition=models.Q(_besluit_url='', _negated=True), fields=('informatieobject', '_besluit_url'), name='unique_io_besluit_external'),
        ),
        migrations.AddIndex(
            model_name='enkelvoudiginformatieobject',
            index=models.Index(fields=['canonical', '-versie'], name='documenten__canonic_31cc4e_idx'),
        ),
        migrations.AddConstraint(
            model_name='enkelvoudiginformatieobject',
            constraint=models.CheckConstraint(check=models.Q(models.Q(models.Q(_informatieobjecttype__isnull=True, _negated=True), ('_informatieobjecttype_url', '')), models.Q(('_informatieobjecttype__isnull', True), models.Q(_informatieobjecttype_url='', _negated=True)), _connector='OR'), name='_informatieobjecttype_or__informatieobjecttype_url_filled'),
        ),
        migrations.AlterUniqueTogether(
            name='enkelvoudiginformatieobject',
            unique_together={('uuid', 'versie')},
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuscripts', '0004_remove_historicalitem_date_sort_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='folio_number',
        ),
        migrations.RemoveField(
            model_name='itemimage',
            name='folio_side',
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='hair_type',
            field=models.CharField(blank=True, choices=[('FHFH', 'FHFH'), ('FHHF', 'FHHF'), ('HFFH', 'HFFH'), ('HFHF', 'HFHF'), ('Mixed', 'Mixed')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='issuer',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='named_beneficiary',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-21 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0035_auto_20200720_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainregistrationorder',
            name='auth_info',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domainregistrationorder',
            name='last_error',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domainregistrationorder',
            name='redirect_uri',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domainregistrationorder',
            name='resource_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='domainregistrationorder',
            name='state',
            field=models.CharField(choices=[('P', 'Pending'), ('T', 'Started'), ('N', 'Needs payment'), ('S', 'Processing'), ('A', 'Pending approval'), ('C', 'Completed'), ('F', 'Failed')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='domainreneworder',
            name='domain_obj',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='domains.DomainRegistration'),
        ),
        migrations.AddField(
            model_name='domainreneworder',
            name='last_error',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domainreneworder',
            name='redirect_uri',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domainreneworder',
            name='resource_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='domainreneworder',
            name='state',
            field=models.CharField(choices=[('P', 'Pending'), ('T', 'Started'), ('N', 'Needs payment'), ('S', 'Processing'), ('A', 'Pending approval'), ('C', 'Completed'), ('F', 'Failed')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='domainrestoreorder',
            name='domain_obj',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='domains.DomainRegistration'),
        ),
        migrations.AddField(
            model_name='domainrestoreorder',
            name='last_error',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domainrestoreorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domainrestoreorder',
            name='redirect_uri',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domainrestoreorder',
            name='resource_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='domainrestoreorder',
            name='state',
            field=models.CharField(choices=[('P', 'Pending'), ('T', 'Started'), ('N', 'Needs payment'), ('S', 'Processing'), ('A', 'Pending approval'), ('C', 'Completed'), ('F', 'Failed')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='domainreneworder',
            name='domain',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domainrestoreorder',
            name='domain',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='domaintransferorder',
            name='state',
            field=models.CharField(choices=[('P', 'Pending'), ('T', 'Started'), ('N', 'Needs payment'), ('S', 'Processing'), ('A', 'Pending approval'), ('C', 'Completed'), ('F', 'Failed')], default='P', max_length=1),
        ),
        migrations.DeleteModel(
            name='PendingDomainTransfer',
        ),
    ]

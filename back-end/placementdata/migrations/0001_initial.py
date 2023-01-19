# Generated by Django 4.1.4 on 2023-01-19 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calender', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('mean_ctc', models.DecimalField(decimal_places=2, max_digits=12)),
                ('highest_ctc', models.DecimalField(decimal_places=2, max_digits=12)),
                ('median_ctc', models.DecimalField(decimal_places=2, max_digits=12)),
                ('number_of_students', models.IntegerField()),
                ('number_of_companies', models.IntegerField()),
                ('number_of_placed', models.IntegerField()),
                ('ug_highest_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('ug_median_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('ug_number_of_students', models.IntegerField(blank=True, null=True)),
                ('ug_number_of_companies', models.IntegerField(blank=True, null=True)),
                ('ug_number_of_placed', models.IntegerField(blank=True, null=True)),
                ('pg_highest_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('pg_median_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('pg_number_of_students', models.IntegerField(blank=True, null=True)),
                ('pg_number_of_companies', models.IntegerField(blank=True, null=True)),
                ('pg_number_of_placed', models.IntegerField(blank=True, null=True)),
                ('calendar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calender.calender')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('allobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
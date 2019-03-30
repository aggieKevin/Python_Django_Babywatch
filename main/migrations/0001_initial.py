# Generated by Django 2.1.7 on 2019-03-30 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('hobby', models.CharField(blank=True, max_length=50)),
                ('allergy', models.CharField(blank=True, max_length=50)),
                ('free_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('drive_license', models.CharField(max_length=30)),
                ('job_type', models.CharField(blank=True, max_length=30)),
                ('company', models.CharField(blank=True, max_length=30)),
                ('relationship', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='guardian',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Household'),
        ),
        migrations.AddField(
            model_name='child',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Household'),
        ),
    ]
# Generated by Django 2.1.7 on 2020-12-05 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('duration', models.DurationField()),
                ('No_of_Subjects', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Roll_no', models.IntegerField()),
                ('DateOfJoining', models.DateField()),
                ('Address', models.CharField(max_length=200)),
                ('PostalCode', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='s_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Student'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-19 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='name',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='password',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='room_no',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='type_of_lab',
        ),
        migrations.RemoveField(
            model_name='lab',
            name='userID',
        ),
        migrations.AddField(
            model_name='lab',
            name='Address',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='Doctor_id',
            field=models.CharField(default='abc', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='Lab_id',
            field=models.CharField(default='pqrs', max_length=6, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='Lab_name',
            field=models.CharField(default='123', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='Password',
            field=models.CharField(default='monika', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='Pincode',
            field=models.CharField(default='deepak', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='Room_No',
            field=models.CharField(default='nupur', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='State',
            field=models.CharField(default='snigdha', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='Type_of_Lab',
            field=models.CharField(default='sagar', max_length=50),
            preserve_default=False,
        ),
    ]

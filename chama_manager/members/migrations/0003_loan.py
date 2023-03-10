# Generated by Django 3.1 on 2040-01-10 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20230105_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]

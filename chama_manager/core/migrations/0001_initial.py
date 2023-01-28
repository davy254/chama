# Generated by Django 3.1 on 2023-01-28 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0006_delete_contribution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('contributed', models.BooleanField(default=False)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]

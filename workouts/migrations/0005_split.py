# Generated by Django 4.0.4 on 2022-05-12 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_exercise_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('inicial_date', models.DateField()),
                ('final_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='workouts.user')),
                ('workouts', models.ManyToManyField(to='workouts.workout')),
            ],
        ),
    ]

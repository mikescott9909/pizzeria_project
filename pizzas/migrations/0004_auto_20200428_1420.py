# Generated by Django 3.0.5 on 2020-04-28 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_topping'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'toppings'},
        ),
        migrations.AlterField(
            model_name='pizza',
            name='text',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza')),
            ],
            options={
                'verbose_name_plural': 'comments',
            },
        ),
    ]

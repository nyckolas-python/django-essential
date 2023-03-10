# Generated by Django 4.1.4 on 2023-03-10 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('model', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=30)),
                ('warranty', models.IntegerField()),
                ('count', models.IntegerField()),
                ('brand_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='nyckolas_shop.brand')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='nyckolas_shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_type', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('end_time', models.DateField(null=True)),
                ('start_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dishwasher',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nyckolas_shop.item')),
                ('energy_saving_class', models.CharField(default='A+', max_length=2)),
                ('power', models.IntegerField(default=0)),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
            ],
            bases=('nyckolas_shop.item',),
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nyckolas_shop.item')),
                ('display', models.DecimalField(decimal_places=4, max_digits=5)),
                ('memory', models.IntegerField()),
                ('video_memory', models.IntegerField()),
                ('cpu', models.CharField(max_length=128)),
            ],
            bases=('nyckolas_shop.item',),
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nyckolas_shop.item')),
                ('display', models.DecimalField(decimal_places=4, max_digits=5)),
                ('memory', models.IntegerField()),
                ('display_type', models.CharField(max_length=8)),
                ('smart_tv', models.BooleanField(verbose_name=False)),
            ],
            bases=('nyckolas_shop.item',),
        ),
        migrations.CreateModel(
            name='VacuumCleaner',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nyckolas_shop.item')),
                ('noise_level', models.FloatField()),
                ('power', models.IntegerField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('eco_engine', models.BooleanField(default=False)),
            ],
            bases=('nyckolas_shop.item',),
        ),
        migrations.AddField(
            model_name='item',
            name='promo',
            field=models.ManyToManyField(to='nyckolas_shop.promo'),
        ),
    ]

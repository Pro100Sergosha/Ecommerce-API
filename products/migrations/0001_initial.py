# Generated by Django 5.0.7 on 2024-08-14 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charging_speed', models.CharField(blank=True, max_length=255, null=True)),
                ('wireless_charging_speed', models.CharField(blank=True, max_length=255, null=True)),
                ('wireless_charging', models.BooleanField(blank=True, null=True)),
                ('battery_life', models.CharField(blank=True, max_length=255, null=True)),
                ('battery_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CameraInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_camera', models.CharField(blank=True, max_length=255, null=True)),
                ('main_camera_video_resolution', models.CharField(blank=True, max_length=255, null=True)),
                ('front_camera_video_resolution', models.CharField(blank=True, max_length=255, null=True)),
                ('front_camera', models.CharField(blank=True, max_length=255, null=True)),
                ('main_camera', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MemoryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_memory', models.CharField(blank=True, max_length=255, null=True)),
                ('memory_standart', models.CharField(blank=True, max_length=255, null=True)),
                ('ram', models.CharField(blank=True, max_length=255, null=True)),
                ('micro_sd_slot', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charging_interface', models.CharField(blank=True, max_length=255, null=True)),
                ('mm3_5', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_type', models.CharField(blank=True, max_length=255, null=True)),
                ('screen_protection', models.CharField(blank=True, max_length=255, null=True)),
                ('resolution', models.CharField(blank=True, max_length=255, null=True)),
                ('refresh_rate', models.CharField(blank=True, max_length=255, null=True)),
                ('screen_brightness', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SizeWeightInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_size', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g5', models.BooleanField(blank=True, null=True)),
                ('e_sim', models.BooleanField(blank=True, null=True)),
                ('sim_card_type', models.CharField(choices=[('no', 'no'), ('dual sim', 'dual sim')], max_length=8)),
                ('stereo_speaker', models.BooleanField(blank=True, null=True)),
                ('bluetooth', models.CharField(blank=True, max_length=255, null=True)),
                ('system_version', models.CharField(blank=True, max_length=255, null=True)),
                ('graphics_proccessor', models.CharField(blank=True, max_length=255, null=True)),
                ('chipset', models.CharField(blank=True, max_length=255, null=True)),
                ('ip_protection', models.CharField(blank=True, max_length=255, null=True)),
                ('build', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('nfc', models.BooleanField(blank=True, null=True)),
                ('battery_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.batteryinfo')),
                ('camera_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.camerainfo')),
                ('memory_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.memoryinfo')),
                ('ports_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.portsinfo')),
                ('screen_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.screeninfo')),
                ('size_weight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.sizeweightinfo')),
                ('technical_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.technicalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('final_price', models.PositiveIntegerField()),
                ('warranty', models.CharField(choices=[('1 month', '1 month'), ('3 month', '3 month'), ('6 month', '6 month'), ('1 year', '1 year'), ('2 year', '2 year')], max_length=7)),
                ('delivery_time', models.CharField(choices=[('1-2 business days', '1-2 business days'), ('3-5 business days', '3-5 business days'), ('5-10 business days', '5-10 business days')], max_length=18)),
                ('stock', models.CharField(choices=[('in stock', 'in stock'), ('out of stock', 'out of stock')], max_length=12)),
                ('quantity', models.PositiveIntegerField()),
                ('date_added', models.DateField()),
                ('additional_images', models.ManyToManyField(related_name='additional_images', to='products.image')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.color')),
                ('color_options', models.ManyToManyField(related_name='color_choices', to='products.color')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.image')),
                ('more_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.moreinfo')),
            ],
        ),
    ]

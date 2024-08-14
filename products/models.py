from django.db import models


class Image(models.Model):
    image = models.ImageField()

class Color(models.Model):
    name = models.CharField(max_length=255)

class TechnicalInfo(models.Model):
    SIM_CARD_CHOICES = (
        ('no', 'no'),
        ('dual sim', 'dual sim')
    )
    g5 = models.BooleanField(blank=True, null=True)
    e_sim = models.BooleanField(blank=True, null=True)
    sim_card_type = models.CharField(max_length=8, choices=SIM_CARD_CHOICES)
    stereo_speaker = models.BooleanField(blank=True, null=True)
    bluetooth = models.CharField(max_length=255, blank=True, null=True)
    system_version = models.CharField(max_length=255, blank=True, null=True)
    graphics_proccessor = models.CharField(max_length=255, blank=True, null=True)
    chipset = models.CharField(max_length=255, blank=True, null=True)
    ip_protection = models.CharField(max_length=255, blank=True, null=True)
    build = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

class SizeWeightInfo(models.Model):
    screen_size = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)

class ScreenInfo(models.Model):
    screen_type = models.CharField(max_length=255, blank=True, null=True)
    screen_protection = models.CharField(max_length=255, blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    refresh_rate = models.CharField(max_length=255, blank=True, null=True)
    screen_brightness = models.CharField(max_length=255, blank=True, null=True)

class MemoryInfo(models.Model):
    internal_memory = models.CharField(max_length=255, blank=True, null=True)
    memory_standart = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    micro_sd_slot = models.BooleanField(blank=True, null=True)

class CameraInfo(models.Model):
    additional_camera = models.CharField(max_length=255, blank=True, null=True)
    main_camera_video_resolution = models.CharField(max_length=255, blank=True, null=True)
    front_camera_video_resolution = models.CharField(max_length=255, blank=True, null=True)
    front_camera = models.CharField(max_length=255, blank=True, null=True)
    main_camera = models.CharField(max_length=255, blank=True, null=True)

class PortsInfo(models.Model):
    charging_interface = models.CharField(max_length=255, blank=True, null=True)
    mm3_5 = models.BooleanField(blank=True, null=True)

class BatteryInfo(models.Model):
    charging_speed = models.CharField(max_length=255, blank=True, null=True)
    wireless_charging_speed = models.CharField(max_length=255, blank=True, null=True)
    wireless_charging = models.BooleanField(blank=True, null=True)
    battery_life = models.CharField(max_length=255, blank=True, null=True)
    battery_type = models.CharField(max_length=255, blank=True, null=True)

class MoreInfo(models.Model):
    technical_info = models.ForeignKey(TechnicalInfo, blank=True, null=True, on_delete=models.CASCADE)
    size_weight = models.ForeignKey(SizeWeightInfo, blank=True, null=True, on_delete=models.CASCADE)
    screen_info = models.ForeignKey(ScreenInfo, blank=True, null=True, on_delete=models.CASCADE)
    memory_info = models.ForeignKey(MemoryInfo, blank=True, null=True, on_delete=models.CASCADE)
    camera_info = models.ForeignKey(CameraInfo, blank=True, null=True, on_delete=models.CASCADE)
    ports_info = models.ForeignKey(PortsInfo, blank=True, null=True, on_delete=models.CASCADE)
    battery_info = models.ForeignKey(BatteryInfo, blank=True, null=True, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    nfc = models.BooleanField(blank=True, null=True)

class Product(models.Model):
    WARRANTY_CHOICES = (
        ('1 month', '1 month'),
        ('3 month', '3 month'),
        ('6 month', '6 month'),
        ('1 year', '1 year'),
        ('2 year', '2 year'),
    )
    DELIVERY_TIME_CHOICES = (
        ('1-2 business days', '1-2 business days'),
        ('3-5 business days', '3-5 business days'),
        ('5-10 business days', '5-10 business days')
    )
    STOCK_CHOICES = (
        ('in stock', 'in stock'),
        ('out of stock', 'out of stock'),
    )
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    final_price = models.PositiveIntegerField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    color_options = models.ManyToManyField(Color, related_name='color_choices')
    additional_images = models.ManyToManyField(Image, related_name='additional_images')
    warranty = models.CharField(max_length=7, choices=WARRANTY_CHOICES)
    delivery_time = models.CharField(max_length=18, choices=DELIVERY_TIME_CHOICES)
    stock = models.CharField(max_length=12, choices=STOCK_CHOICES)
    quantity = models.PositiveIntegerField()
    date_added = models.DateField()
    more_info = models.ForeignKey(MoreInfo, on_delete=models.CASCADE, blank=True, null=True)
from django.db import models

from Utils.models import Style, Palette, Material, Photos


class Product(models.Model):
    HANDLE_OPTIONS = [
        ('ST', 'Standard'),
        ('HD', 'Hidden'),
    ]

    # main part
    title = models.CharField(max_length=100)
    description_shorted = models.CharField(max_length=200)
    description_full = models.TextField(max_length=10000)
    main_photo = models.ImageField(upload_to='designs', max_length=500)

    # partition part
    photos = models.ManyToManyField(Photos)
    styles = models.ManyToManyField(Style)
    palette = models.ManyToManyField(Palette)
    materials = models.ManyToManyField(Material)
    handle = models.CharField(max_length=2, choices=HANDLE_OPTIONS, default='ST')

    # utility part
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

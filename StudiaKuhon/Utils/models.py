from django.db import models


class Photos(models.Model):
    photo = models.ImageField(upload_to='designs/% Y/% m/% d/', max_length=500)


class Style(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Palette(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

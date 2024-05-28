from django.db import models

# Create your models here.
class BenefitCard(models.Model):
    card_img = models.URLField()
    card_title = models.CharField(max_length=16)
    card_desc = models.CharField(max_length=80)


class Testimonial(models.Model):
    photo = models.FileField()
    name = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    testimonial = models.CharField(max_length=550)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class IceCream(models.Model):
    img = models.URLField()
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=800)
    price = models.FloatField()
    old_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

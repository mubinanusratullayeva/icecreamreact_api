from django.contrib import admin

from .models import Category, IceCream, Testimonial, BenefitCard

# Register your models here.
admin.site.register(Category)
admin.site.register(IceCream)
admin.site.register(BenefitCard)
admin.site.register(Testimonial)
from rest_framework import serializers
from .models import Category, IceCream, Testimonial, BenefitCard


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class BenefitCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitCard
        fields = '__all__'

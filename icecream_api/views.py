from rest_framework import viewsets
from .models import Category, IceCream, Testimonial, BenefitCard
from .serializers import CategorySerializer, BenefitCardSerializer, TestimonialSerializer, IceCreamSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IceCreamViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class BenefitCardViewSet(viewsets.ModelViewSet):
    queryset = BenefitCard.objects.all()
    serializer_class = BenefitCardSerializer

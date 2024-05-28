from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, IceCreamViewSet, TestimonialViewSet, BenefitCardViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('icecreams', IceCreamViewSet)
router.register('testimonials', TestimonialViewSet)
router.register('benefitcards', BenefitCardViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
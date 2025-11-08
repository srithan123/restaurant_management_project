from django.urls import path
from .views import *

urlpatterns = [
    path('coupons/validate/',CouponValidation.as_view(),name='coupon_validate'),
]
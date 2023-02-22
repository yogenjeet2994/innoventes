from django.urls import  path
from .views import CompanyList, CompanyDetail


urlpatterns = [

    path('cmp/', CompanyList.as_view(), name='company_list'),
    path('cmp/<str:pk>/', CompanyDetail.as_view(), name='company_details')
]
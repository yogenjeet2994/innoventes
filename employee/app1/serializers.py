from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'email_id', 'company_code', 'strength', 'website', 'created_time')
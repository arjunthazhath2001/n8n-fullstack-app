from rest_framework import serializers


BUDGET_CHOICES=['0-100','100-1000','1000+']

class InputSerializer(serializers.Serializer):
    first_name= serializers.CharField()
    last_name= serializers.CharField()
    email= serializers.EmailField()
    budget= serializers.ChoiceField(choices=BUDGET_CHOICES)
    message=serializers.CharField()
    
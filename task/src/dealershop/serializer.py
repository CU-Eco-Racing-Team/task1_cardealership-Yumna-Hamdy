from rest_framework import  serializers
from .models import *

class Dealers_serializer(serializers.ModelSerializer):
    class Meta:
        model = Dealers
        fields = ['Name','SSN',  'phone']
        depth =1



class Contract_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['Start_Date', 'End_Date', 'Dealers']
        extra_kwargs = {'Dealers': {'read_only': True}}


class Industries_serializer(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = ['Name', 'phone', 'Cars']

class Customers_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'       
        
class Cars_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['Price','Model','Plate_No']
        extra_kwargs = {'Customer': {'read_only': True},'Industries': {'read_only': True}}


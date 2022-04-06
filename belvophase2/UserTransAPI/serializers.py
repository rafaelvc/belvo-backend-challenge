from rest_framework import serializers
from .models import User, Transactions

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'

    def validate(self, data):
        if data['type'] == "inflow" and data['amount'] < 0:
            raise serializers.ValidationError("Inflow transaction " + data['reference'] + " must be positive.")
        if data['type'] == "outflow" and data['amount'] > 0:
            raise serializers.ValidationError("Outflow transaction " + data['reference'] + " must be negative.")
        if data['type'] != "inflow" and data['type'] != "outflow": 
            raise serializers.ValidationError("Invalid type of transaction for (" + data['reference'] + \
                 "). Type was (" + data['type'] + ") and it must be inflow or outflow.")
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UsersAgeSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
       print (instance)
       return {
           'total_age': instance['age__sum'],
        }

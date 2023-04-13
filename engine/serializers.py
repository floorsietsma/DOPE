from django.contrib.auth.models import User, Group
from rest_framework import serializers
from engine.models import Machine, Factory, Product, LineStep
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    factories = serializers.PrimaryKeyRelatedField(many=True, queryset=Factory.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'factories']


class FactorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Factory
        fields = ['name', 'description', 'user']


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['name', 'description', 'costPerMinute', 'buildDate', 'factory']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'materialCost']


class LineStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineStep
        fields = ['product', 'machine', 'order', 'leadTimeSeconds']


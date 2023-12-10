from rest_framework import serializers

from vehicle.models import Car, Moto


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        # выбираем поля fields = (title, description) или все fields = '__all__'
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moto
        # выбираем поля fields = (title, description) или все fields = '__all__'
        fields = '__all__'

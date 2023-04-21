from django.contrib.auth.models import User
from rest_framework import serializers
from App_User.models import Student, Category, Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # exclude = ['uuid']
        fields = '__all__'

    def validate(self, data):
        if 'age' in data:
            if data['age'] < 18:
                raise serializers.ValidationError({'age': "age cannot be less than 18"})

        if 'first_name' in data:
            if data['first_name']:
                for n in data['first_name']:
                    if n.isdigit():
                        raise serializers.ValidationError({'first_name': 'Numeric value not allow!'})
                if len(data['first_name']) < 3:
                    raise serializers.ValidationError({'first_name': 'minimum 3 characters Required!'})

        if 'last_name' in data:
            if data['last_name']:
                for n in data['last_name']:
                    if n.isdigit():
                        raise serializers.ValidationError({'last_name': 'Numeric value not allow!'})
                if len(data['last_name']) < 3:
                    raise serializers.ValidationError({'last_name': 'minimum 3 characters Required!'})

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'

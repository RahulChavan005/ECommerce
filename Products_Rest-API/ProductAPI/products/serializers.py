from rest_framework import serializers
from .models import *

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id','productname','price','description','category','categories')

    # def get_fields(self):
    #     fields = super(productSerialzer, self).get_fields()
    #     fields['category'] =  ', '.join([a.name for a in self.category.all()]) 
    #     return fields


class categorySerialzer(serializers.ModelSerializer):

    class Meta:
        model = Category
        #fields = '__all__'
        fields = ('id','name','parent','children')

    def get_fields(self):
        fields = super(categorySerialzer, self).get_fields()
        fields['children'] = categorySerialzer(many=True,read_only=True)
        return fields

    # def create(self, validated_data):
    #     children_data = validated_data.pop('children')
    #     category = Category.objects.create(**validated_data)
    #     Category.objects.create(category=category, **children_data)
    #     return category


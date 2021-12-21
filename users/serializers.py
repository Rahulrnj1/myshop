from rest_framework import serializers
from users.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name','price','description','type','details',) 
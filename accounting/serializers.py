from rest_framework import serializers
from .models import Bill, Payment

class BillSerializers(serializers.ModelSerializer):
  class Meta:
    model = Bill
    fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = '__all__'
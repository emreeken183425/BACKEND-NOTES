from rest_framework import serializers
from .models import Todo,Category
from django.utils.timezone import now

class TodoSerializers(serializers.ModelSerializer):
    days=serializers.SerializerMethodField()
    #category=serializers.StringRelatedField()
    class Meta:
        model=Todo
        fields="__all__"
    #!object level validation ekleme yaptık todo içine  
    def get_days(self,obj):
        return(now()-obj.createDate).days    
    
    def validate_task(self,value):
        if value.lower()=='python':
            raise serializers.ValidationError("python cannot be our test")
    
        
class CategorySerializers(serializers.ModelSerializer):
    #related name
   # categorys=TodoSerializers(many=True )# todo içindeki tüm verileri getiriyor
    categorys=serializers.StringRelatedField(many=True )# self deki string ifadeyi görmek için bu method
    
    class Meta:
        model=Category
        fields="__all__"        




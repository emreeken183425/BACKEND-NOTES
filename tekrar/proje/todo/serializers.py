from dataclasses import fields
from rest_framework import serializers
from django.utils.timezone import now
from .models import Todo, Category





class TodoSerializers(serializers.ModelSerializer):

    days = serializers.SerializerMethodField()

    category = serializers.StringRelatedField() # buradaki "category" todo modelindeki field, default olarak id veriyor, biz burada str ile tanımlananı kullandık.

    class Meta:
        model = Todo
        fields = "__all__"

    # get_ sabit gelen buraya tanımlamak istediğimiz fieldi yazdık. buradaki "days" yukarıda tanımladığımız serializermethodfield dan geldi
    def get_days(self, obj):
        return (now()- obj.createDate).days

    # validate_.buraya meldeki fiedi yaz(self, value).  gerisi sabit
    def validate_task(self, value):
        if value.lower() == "python":
            raise serializers.ValidationError("python can not be our task") 
        return        






class CategorySerializers(serializers.ModelSerializer):

    # related_name="categorys" deki categorys i aldık
    categorys = TodoSerializers(many=True) # tüm todo geldi
    # categorys = serializers.StringRelatedField(many=True) # sadce str methodu geldi
    # categorys = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # id ile geldi
    class Meta :
        model=Category
        fields="__all__"
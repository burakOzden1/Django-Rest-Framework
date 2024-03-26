from rest_framework import serializers
from haberler.models import Makale


class MakaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayimlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    olusturulma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_date):
        print(validated_date)
        return Makale.objects.create(**validated_date)

    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayimlanma_tarihi = validated_data.get('yayimlanma_tarihi', instance.yayimlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance
        
    def validate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Baslik ve aciklama alanlari ayni olamaz.')
        return data
    
    def validate_baslik(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(f'Baslik alani minimum 20 karakter olmali. Siz {len(value)} karakter girdiniz.')
        return value
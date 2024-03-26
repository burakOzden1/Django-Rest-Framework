from rest_framework import serializers
from haberler.models import Makale, Gazeteci

from datetime import datetime, date
from django.utils.timesince import timesince

class MakaleSerializer(serializers.ModelSerializer):

    time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()
    # yazar = GazeteciSerializer()

    class Meta:
        model = Makale
        fields = '__all__'
        # fields = ['yazar', 'baslik', 'aciklama']
        # exclude = ['yazar', 'baslik', 'aciklama'] # ifadesi ile bu alanlar disinda kalan tum ifadeleri aliriz.
        read_only_fields = ['id', 'olusturulma_tarihi', 'guncellenme_tarihi']

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.yayimlanma_tarihi
        if object.aktif == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Aktif Değil!'
    
    def validate_yayimlanma_tarihi(self, tarihDegeri):
        today = date.today()
        if tarihDegeri > today:
            raise serializers.ValidationError('Yayimlanma tarihi ileri bir tarih olamaz!')
        return tarihDegeri



class GazeteciSerializer(serializers.ModelSerializer):

    # makaleler = MakaleSerializer(many=True, read_only=True)
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )
    class Meta:
        model = Gazeteci
        fields = '__all__'


##################### STANDART SERIALIZER #####################
# class MakaleDefaultSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     yazar = serializers.CharField()
#     baslik = serializers.CharField()
#     aciklama = serializers.CharField()
#     metin = serializers.CharField()
#     sehir = serializers.CharField()
#     yayimlanma_tarihi = serializers.DateField()
#     aktif = serializers.BooleanField()
#     olusturulma_tarihi = serializers.DateTimeField(read_only=True)
#     guncellenme_tarihi = serializers.DateTimeField(read_only=True)

#     def create(self, validated_date):
#         print(validated_date)
#         return Makale.objects.create(**validated_date)

#     def update(self, instance, validated_data):
#         instance.yazar = validated_data.get('yazar', instance.yazar)
#         instance.baslik = validated_data.get('baslik', instance.baslik)
#         instance.aciklama = validated_data.get('aciklama', instance.aciklama)
#         instance.metin = validated_data.get('metin', instance.metin)
#         instance.sehir = validated_data.get('sehir', instance.sehir)
#         instance.yayimlanma_tarihi = validated_data.get('yayimlanma_tarihi', instance.yayimlanma_tarihi)
#         instance.aktif = validated_data.get('aktif', instance.aktif)
#         instance.save()
#         return instance
        
#     def validate(self, data):
#         if data['baslik'] == data['aciklama']:
#             raise serializers.ValidationError('Baslik ve aciklama alanlari ayni olamaz.')
#         return data
    
#     def validate_baslik(self, value):
#         if len(value) < 20:
#             raise serializers.ValidationError(f'Baslik alani minimum 20 karakter olmali. Siz {len(value)} karakter girdiniz.')
#         return value
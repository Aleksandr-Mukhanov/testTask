from rest_framework import serializers
from .models import Blocks, Pages


class SerailizerPages(serializers.ModelSerializer):
    slag = serializers.SerializerMethodField()

    def get_slag(self, pages):
        request = self.context.get('request')
        slag_url = pages.slag
        return request.build_absolute_uri(slag_url)

    class Meta:
        model = Pages
        fields = ('id', 'name', 'slag')


class SerailizerBlocks(serializers.ModelSerializer):
    class Meta:
        model = Blocks
        fields = ('id', 'name', 'videoURL', 'qntView')

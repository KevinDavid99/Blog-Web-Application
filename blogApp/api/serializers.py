from rest_framework.serializers import ModelSerializer
from blogApp.models import Post


class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'image', 'title', 'content' ]


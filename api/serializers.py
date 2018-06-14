from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Like, Pin


class RoundingDecimalField(serializers.DecimalField):
    def validate_precision(self, value):
        """
        Code from https://github.com/encode/django-rest-framework/blob/master/rest_framework/fields.py
        Here, we get rid of the max_decimal_places check so that it rounds
        automatically if there are too many decimal places.
        """  # noqa
        sign, digittuple, exponent = value.as_tuple()
        if exponent >= 0:
            # 1234500.0
            total_digits = len(digittuple) + exponent
            whole_digits = total_digits
            decimal_places = 0
        elif len(digittuple) > abs(exponent):
            # 123.45
            total_digits = len(digittuple)
            whole_digits = total_digits - abs(exponent)
            decimal_places = abs(exponent)
        else:
            # 0.001234
            total_digits = abs(exponent)
            whole_digits = 0
            decimal_places = total_digits

        if self.max_digits is not None and total_digits > self.max_digits:
            self.fail('max_digits', max_digits=self.max_digits)

        if (self.max_whole_digits is not None and
                whole_digits > self.max_whole_digits):
            self.fail('max_whole_digits',
                      max_whole_digits=self.max_whole_digits)

        return value


class PinSerializer(serializers.HyperlinkedModelSerializer):
    lat_field = Pin._meta.get_field('latitude')
    lng_field = Pin._meta.get_field('longitude')

    latitude = RoundingDecimalField(max_digits=lat_field.max_digits,
                                    decimal_places=lat_field.decimal_places)
    longitude = RoundingDecimalField(max_digits=lng_field.max_digits,
                                     decimal_places=lng_field.decimal_places)
    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text',
        source='comment_set'
    )
    likes = serializers.IntegerField(
        source='like_set.count',
        read_only=True,
    )

    class Meta:
        model = Pin
        fields = ('id', 'pin_type', 'latitude', 'longitude', 'created_at',
                  'comments', 'likes')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pin', 'text', 'created_at')


class LikeSerializer(serializers.ModelSerializer):
    by_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Like
        fields = ('id', 'pin', 'created_at', 'by_user')
        validators = [
            UniqueTogetherValidator(
                queryset=Like.objects.all(),
                fields=('pin', 'by_user')
            )
        ]

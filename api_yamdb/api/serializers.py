from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework.serializers import (CharField, ModelSerializer, Serializer,
                                        ValidationError)
from reviews.models import Category, Genre, Title
from users.models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )

    def validate_username(self, value):
        if (value == 'me'):
            raise ValidationError(
                'Запрещено использовать me в качестве username.'
            )
        return value


class NotAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('role',)


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        if (value == 'me'):
            raise ValidationError(
                'Запрещено использовать me в качестве username.'
            )
        return value


class TokenSerializer(Serializer):
    username = CharField(
        max_length=150, validators=[UnicodeUsernameValidator, ]
    )
    confirmation_code = CharField()


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class TitleSerializer(ModelSerializer):
    class Meta:
        model = Title
        fields = (
            'name',
            'description',
            'year',
            'rating',
            'genre',
            'category',
        )

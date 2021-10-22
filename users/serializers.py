from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        exclude=["id"]

class SignUpSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = [
            "email",
            "password"
        ]

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user